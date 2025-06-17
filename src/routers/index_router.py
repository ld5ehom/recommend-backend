from fastapi import APIRouter, Depends, status, Response

from src.schemas import user_schema
from src.schemas import access_token_schema
from src.services import user_service

"""
Authentication router that handles user login and registration endpoints.
사용자 로그인 및 회원가입 엔드포인트를 처리하는 인증 라우터입니다.
"""
# Initialize API router with tag "Authentication"
# "Authentication" 태그로 API 라우터 초기화
router = APIRouter(tags=["Authentication"])

# Handle user login and return access token
# 사용자 로그인을 처리하고 액세스 토큰을 반환합니다
@router.post("/login")
async def login_user(access_token: access_token_schema.AccessToken = Depends(user_service.authenticate_user)):
    return {
        "access_token": access_token.access_token,
        "token_type": "bearer"
    }


"""
# (Optional) Invalidate access token by clearing cookie (not active)
# (선택 사항) 액세스 토큰을 무효화하기 위해 쿠키를 삭제 (현재 비활성화됨)
@router.get("/logout")
async def logout_user(response: Response):
    response.delete_cookie(key="access_token")
    return response
"""

# Handle new user registration and return user info
# 새로운 사용자 회원가입을 처리하고 사용자 정보를 반환합니다
@router.post("/signup", response_model=user_schema.User)
async def create_user(user: user_schema.User = Depends(user_service.add_user)):
    return user
