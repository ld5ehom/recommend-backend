from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, Integer, DateTime, Text
from sqlalchemy.orm import relationship

from src.core.database import Base

"""
Defines the AccessToken model used for user authentication sessions.
Stores access tokens with expiration time, linked to a specific user.
사용자 인증 세션을 위한 AccessToken 모델을 정의합니다.
특정 사용자와 연결된 액세스 토큰과 만료 시간을 저장합니다.
"""

# Represents a user access token entry in the system
# 사용자 액세스 토큰 정보를 나타내는 모델
class AccessToken(Base):
    __tablename__ = "user_access_tokens"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey("auth_user.id"), nullable=False)
    access_token = Column(Text, nullable=False)
    expiration_date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="access_token")
