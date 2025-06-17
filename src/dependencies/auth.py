from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt

from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

import src.core.auth as AUTH

"""
Authentication utility functions for hashing passwords, creating JWT tokens,
and extracting user identity from access tokens.

비밀번호 해싱, JWT 토큰 생성, 액세스 토큰에서 사용자 정보 추출을 위한 인증 유틸리티 함수들을 정의합니다.
"""
# Password hashing context using bcrypt algorithm
# bcrypt 알고리즘을 사용하는 비밀번호 해시 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 bearer token scheme (used in dependency injection)
# OAuth2 베어러 토큰 스킴 (의존성 주입에 사용됨)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Verify that the plain password matches the hashed password
# 입력된 평문 비밀번호가 해시된 비밀번호와 일치하는지 확인
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Hash the input password using bcrypt
# 입력된 비밀번호를 bcrypt로 해싱
def get_password_hash(password):
    return pwd_context.hash(password)


# Create a signed JWT access token
# JWT 액세스 토큰 생성 (서명 포함)
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        AUTH.AUTH_SECRET_KEY,
        algorithm=AUTH.AUTH_ALGORITHM
    )

    return encoded_jwt


# Decode access token and extract username ("sub" claim)
# 액세스 토큰을 디코딩하고 사용자 이름("sub" 클레임)을 추출
def get_access_token_data(access_token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            access_token,
            AUTH.AUTH_SECRET_KEY,
            algorithms=[AUTH.AUTH_ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        
    except JWTError:
        raise credentials_exception
    
    return username

# Retrieve the configured expiration duration for access tokens
# 설정된 액세스 토큰 만료 시간을 반환
def get_access_token_expire_minutes():
    return AUTH.AUTH_ACCESS_TOKEN_EXPIRE_MINUTES
