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
    user_model, restaurant_model, access_token_model
)
from src.schemas import user_schema, access_token_schema

"""
Provides user-related services including authentication, profile management,
follow/like services, and user data retrieval and updates.
사용자 인증, 프로필 관리, 팔로우/좋아요 기능, 사용자 데이터 조회 및 수정 기능을 제공합니다.
"""
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
    Register a new user. (새 사용자를 등록합니다)
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
