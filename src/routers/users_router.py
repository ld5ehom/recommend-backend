from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.dependencies.database import get_db
from src.dependencies.auth import oauth2_scheme
from src.schemas import user_schema
from src.services import user_service  

"""
Defines API endpoints for user-related actions such as profile management, following, and liking.
사용자 프로필 관리, 팔로우, 좋아요 등의 기능을 제공하는 API 엔드포인트를 정의합니다.
"""
router = APIRouter(tags=["Users"])

# Get all users / 모든 사용자 조회
@router.get("/", 
            response_model=list[user_schema.UserSearchResult])
async def read_users(users: list[user_schema.User] = Depends(user_service.get_users)):
    return users

# Get current user info / 현재 로그인한 사용자 정보 조회
@router.get("/me", 
            response_model=user_schema.User, 
            dependencies=[Depends(oauth2_scheme)])
async def read_current_user(current_user: user_schema.User = Depends(user_service.get_current_user)):
    return current_user

# Update current user info / 현재 로그인한 사용자 정보 수정
@router.put("/me", 
            response_model=user_schema.User, 
            dependencies=[Depends(oauth2_scheme)])
async def update_current_user(current_user: user_schema.UserUpdate = Depends(user_service.edit_current_user)):
    return current_user

# Follow
# Follow another user / 다른 사용자 팔로우
@router.post("/me/followings", 
             response_model=user_schema.UserSearchResult, 
             dependencies=[Depends(oauth2_scheme)])
async def create_current_user_followings(user: user_schema.UserSearchResult = Depends(user_service.add_current_user_following)):
    return user

# Get followings of current user / 현재 사용자가 팔로우한 사용자 목록 조회
@router.get("/me/followings", 
            response_model=list[user_schema.UserSearchResultSimple], 
            dependencies=[Depends(oauth2_scheme)])
async def read_current_user_followings(users: list[user_schema.UserSearchResultSimple] = Depends(user_service.get_current_user_followings)):
    return users

# Unfollow a user / 사용자 언팔로우
@router.delete("/me/followings", 
               response_model=user_schema.UserSearchResult, 
               dependencies=[Depends(oauth2_scheme)])
async def delete_current_user_followings(user: user_schema.UserSearchResult = Depends(user_service.remove_current_user_following)):
    return user

# Get followers of current user / 현재 사용자 팔로워 목록 조회
@router.get("/me/followers", 
            response_model=list[user_schema.UserSearchResultSimple], 
            dependencies=[Depends(oauth2_scheme)])
async def read_current_user_followers(users: list[user_schema.UserSearchResultSimple] = Depends(user_service.get_current_user_followers)):
    return users


# {id}
# Get a specific user by ID / 특정 사용자 ID로 조회
@router.get("/{id}", 
            response_model=user_schema.UserSearchResult)
async def read_user(user: user_schema.UserSearchResult = Depends(user_service.get_user_by_id)):
    return user

# Get followings of specific user / 특정 사용자가 팔로우한 목록 조회
@router.get("/{id}/followings", 
            response_model=list[user_schema.UserSearchResultSimple])
async def read_user_followings(followings: list[user_schema.UserSearchResultSimple] = Depends(user_service.get_followings_by_id)):
    return followings

# Get followers of specific user / 특정 사용자의 팔로워 목록 조회
@router.get("/{id}/followers", 
            response_model=list[user_schema.UserSearchResultSimple])
async def read_user_followers(followers: list[user_schema.UserSearchResultSimple] = Depends(user_service.get_followers_by_id)):
    return followers

