from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from typing import cast
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.dependencies.auth import (
    oauth2_scheme, verify_password, get_password_hash,
    create_access_token, get_access_token_data, get_access_token_expire_minutes
)
from src.dependencies.database import get_db

from sqlalchemy.orm import Session
from src.models import (
    user_model, restaurant_model, access_token_model, user_follow_model, user_like_model
)
from src.schemas import user_schema, access_token_schema


"""
Provides user-related services including authentication, profile management,
follow/like services, and user data retrieval and updates.
사용자 인증, 프로필 관리, 팔로우/좋아요 기능, 사용자 데이터 조회 및 수정 기능을 제공합니다.
"""
# -------------------- BASIC USER FUNCTIONS --------------------
def get_current_user(access_token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Retrieve current user using access token.
    액세스 토큰을 통해 현재 사용자를 조회합니다.
    """
    return get_user_by_username(get_access_token_data(access_token), db)


def get_user_by_id(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a user by ID.
    ID로 사용자를 조회합니다.
    """
    user = db.query(user_model.User).filter(user_model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return user


def get_user_by_username(username: str, db: Session = Depends(get_db)):
    """
    Retrieve a user by username.
    사용자명을 기준으로 사용자를 조회합니다.
    """
    return db.query(user_model.User).filter(user_model.User.username == username).first()


def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all users with optional pagination.
    페이지네이션을 통해 전체 사용자 목록을 조회합니다.
    """
    return db.query(user_model.User).offset(skip).limit(limit).all()


def add_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.
    새 사용자를 등록합니다.
    """
    if get_user_by_username(user.username, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exist")

    db_user = user_model.User(
        username=user.username,
        password=get_password_hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        nickname='',
        bio='',
        is_superuser=False,
        is_staff=False,
        is_active=True,
        date_joined=datetime.now()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# -------------------- FOLLOW FUNCTIONS --------------------
def add_following(user_id, target_user_id, db: Session = Depends(get_db)):
    """
    Add a following relationship.
    팔로잉 관계를 추가합니다.
    """
    target_user = get_user_by_id(target_user_id, db)
    if not target_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    db_following = user_follow_model.UserFollow(
        user_id=user_id,
        target_user_id=target_user_id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(db_following)
    db.commit()
    db.refresh(db_following)

    return target_user


def add_current_user_following(target_user_id: int, current_user: user_schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Add following for the current user. 
    """
    return add_following(current_user.id, target_user_id, db)


def remove_following(user_id, target_user_id, db: Session = Depends(get_db)):
    """
    Remove a following relationship. 
    """
    target_user = get_user_by_id(target_user_id, db)
    if not target_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    db_following = db.query(user_follow_model.UserFollow).filter(
        user_follow_model.UserFollow.user_id == user_id,
        user_follow_model.UserFollow.target_user_id == target_user_id
    ).first()

    db.delete(db_following)
    db.commit()

    return target_user


def remove_current_user_following(target_user_id: int, current_user: user_schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Remove following for current user.
    """
    return remove_following(current_user.id, target_user_id, db)




# -------------------- GET FOLLOW/LIKE LISTS --------------------
def get_followings_by_id(id: int = 0, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get followings by user ID.
    사용자의 팔로잉 목록을 조회합니다.
    """
    following_ids = db.query(user_follow_model.UserFollow).filter(
        user_follow_model.UserFollow.user_id == id
    ).offset(skip).limit(limit).all()

    followings = db.query(user_model.User).filter(
        user_model.User.id.in_([x.target_user_id for x in following_ids])
    ).offset(skip).limit(limit).all()

    return followings


def get_followers_by_id(id: int = 0, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get followers by user ID.
    사용자의 팔로워 목록을 조회합니다.
    """
    follower_ids = db.query(user_follow_model.UserFollow).filter(
        user_follow_model.UserFollow.target_user_id == id
    ).offset(skip).limit(limit).all()

    followers = db.query(user_model.User).filter(
        user_model.User.id.in_([x.user_id for x in follower_ids])
    ).offset(skip).limit(limit).all()

    return followers


def get_likes_by_id(id: int = 0, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get liked restaurants by user ID.
    사용자가 좋아요한 식당 목록을 조회합니다.
    """
    restaurant_ids = db.query(user_like_model.UserLike).filter(
        user_like_model.UserLike.user_id == id
    ).offset(skip).limit(limit).all()

    restaurants = db.query(restaurant_model.Restaurant).filter(
        restaurant_model.Restaurant.id.in_([x.restaurant_id for x in restaurant_ids])
    ).offset(skip).limit(limit).all()

    return restaurants


def get_current_user_followings(current_user: user_schema.User = Depends(get_current_user), skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get followings for current user.
    현재 사용자의 팔로잉 목록을 조회합니다.
    """
    return get_followings_by_id(current_user.id, skip, limit, db)


def get_current_user_followers(current_user: user_schema.User = Depends(get_current_user), skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get followers for current user.
    현재 사용자의 팔로워 목록을 조회합니다.
    """
    return get_followers_by_id(current_user.id, skip, limit, db)


def get_current_user_likes(current_user: user_schema.User = Depends(get_current_user), skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get likes for current user.
    현재 사용자가 좋아요한 식당 목록을 조회합니다.
    """
    return get_likes_by_id(current_user.id, skip, limit, db)


# -------------------- USER UPDATE --------------------
def edit_user(id: int, user: user_schema.UserUpdate, db: Session = Depends(get_db)):
    """
    Update user information by ID.
    ID로 사용자의 정보를 수정합니다.
    """
    db_user = get_user_by_id(id, db)
    if db_user is None:
        raise Exception("User not exist")

    for key, val in user:
        if key == "password":
            val = get_password_hash(val)
        setattr(db_user, key, val)

    db.commit()
    db.refresh(db_user)

    return db_user


def edit_current_user(user: user_schema.UserUpdate, current_user: user_schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Update current user information.
    현재 사용자의 정보를 수정합니다.
    """
    return edit_user(current_user.id, user, db)


# -------------------- BATCH USER CREATION --------------------
def add_users(users: list[user_schema.UserCreate], db: Session = Depends(get_db)):
    """
    Add multiple users (for testing).
    여러 사용자를 한 번에 추가합니다 (테스트용).
    """
    db_users = []
    for user in users:
        if get_user_by_username(user.username, db):
            raise Exception("User already exist")
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = user_model.User(
            username=user.username,
            password=fake_hashed_password,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            is_superuser=False,
            is_staff=False,
            is_active=True,
            date_joined=datetime.now()
        )
        db_users.append(db_user)

    db.add_all(db_users)
    db.commit()

    for db_user in db_users:
        db.refresh(db_user)

    return db_users

def authenticate_user(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate and issue access token.
    사용자 인증 후 액세스 토큰을 발급합니다.
    """
    user = get_user_by_username(form_data.username, db)
    if user is None or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    expires_delta = timedelta(minutes=get_access_token_expire_minutes())
    expiration_date = datetime.now() + expires_delta

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=expires_delta
    )

    db_token = access_token_model.AccessToken(
        user_id=user.id,
        access_token=access_token,
        expiration_date=expiration_date
    )
    db.add(db_token)
    user.last_login = datetime.now()
    db.commit()
    db.refresh(db_token)

    return cast(access_token_schema.AccessToken, db_token)

