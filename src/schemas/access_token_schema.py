from datetime import datetime

from pydantic import BaseModel

from src.schemas import user_schema

"""
Defines Pydantic schemas for AccessToken entity used in authentication.
인증에서 사용되는 AccessToken 엔터티를 위한 Pydantic 스키마를 정의합니다.
"""
class AccessTokenBase(BaseModel):
    # Unique identifier of the access token
    # 액세스 토큰의 고유 식별자
    id: int

    # ID of the user associated with this token
    # 이 토큰과 연관된 사용자의 ID
    user_id: int

    # The token string value
    # 토큰 문자열 값
    access_token: str

    # Expiration timestamp of the token. 토큰의 만료 시각
    expiration_date: datetime

    class Config:
        from_attributes = True

# Base schema without user info
# 사용자 정보 없이 기본 스키마만 사용
class AccessToken(AccessTokenBase):
    pass

# Extended schema with user information
# 사용자 정보를 포함한 확장된 스키마
class AccessTokenWithUser(AccessTokenBase):
    user: user_schema.User | None = None
