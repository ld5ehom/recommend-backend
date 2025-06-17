from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.core.database import Base

"""
Defines the User model for authentication and profile management.
사용자 인증 및 프로필 관리를 위한 User 모델을 정의합니다.
"""
class User(Base):
    __tablename__ = "auth_user"

    # Primary key , username and password for each user
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    # User's first and last name
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    # User's email address
    email = Column(String, nullable=False)

    # Optional nickname for display / 표시용 닉네임 (선택 항목)
    nickname = Column(String, nullable=True)

    # Optional biography/introduction
    # 사용자 소개글 또는 자기소개 (선택 항목)
    bio = Column(String, nullable=True)

    # Flag for superuser status / 슈퍼유저 여부를 나타내는 플래그
    is_superuser = Column(Boolean, nullable=False)

    # Flag for staff (admin panel access) / 관리자 권한 여부를 나타내는 플래그
    is_staff = Column(Boolean, nullable=False)

    # Active user flag (used for login) / 사용자 활성 여부 (로그인 가능 여부)
    is_active = Column(Boolean, nullable=False)

    # Last login timestamp / 마지막 로그인 시간
    last_login = Column(DateTime, nullable=True)

    # Timestamp of user creation / 사용자 계정 생성 시각
    date_joined = Column(DateTime, nullable=False)

    # One-to-one relationship to access token
    # 액세스 토큰과의 일대일 관계
    access_token = relationship("AccessToken", back_populates="user")

    # One-to-many: restaurants liked by the user
    # 사용자가 좋아요한 음식점과의 일대다 관계
    like_restaurants = relationship("UserLike", back_populates="user")

    # (Future use) Following relationships
    # (추후 사용) 사용자 팔로우 관계
    # followings = relationship("UserFollow", back_populates="user", foreign_keys=['users_follows_users.user_id'])
    # followers = relationship("UserFollow", back_populates="target_user", foreign_keys=['users_follows_users.target_user_id'])
