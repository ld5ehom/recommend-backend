from datetime import datetime
from typing import List
from pydantic import BaseModel

"""
Defines Pydantic schemas for user-related data models.
Used for data validation and serialization of user info in API endpoints.
사용자 관련 데이터 모델을 위한 Pydantic 스키마 정의.
API에서 사용자 정보의 유효성 검사 및 직렬화에 사용됨.
"""
# Base user schema with common user fields
# 공통 사용자 필드를 포함하는 기본 스키마
class UserBase(BaseModel):
    username: str

    class Config:
        from_attributes = True

# Schema for user login
# 사용자 로그인 요청을 위한 스키마
class UserLogin(UserBase):
    password: str

# Schema for user registration
# 사용자 회원가입 요청을 위한 스키마
class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str
    email: str

# Schema for user profile update
# 사용자 프로필 업데이트 요청을 위한 스키마
class UserUpdate(UserCreate):
    nickname: str
    bio: str

# Simplified schema for user search results
# 사용자 검색 결과에 사용되는 간단한 스키마
class UserSearchResultSimple(UserBase):
    id: int
    nickname: str

# Full schema for user search results
# 사용자 검색 결과에 사용되는 전체 스키마
class UserSearchResult(UserSearchResultSimple):
    bio: str
    last_login: datetime | None = None
    date_joined: datetime

# Full user schema for output representation
# 사용자 정보를 나타내는 전체 출력 스키마
class User(UserBase):
    id: int
    first_name: str
    last_name: str
    email: str
    nickname: str
    bio: str

    is_superuser: bool
    is_staff: bool
    is_active: bool

    last_login: datetime | None = None
    date_joined: datetime
