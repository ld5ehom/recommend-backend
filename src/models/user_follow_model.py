import datetime
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base
from src.models import user_model

"""
Defines the UserFollow model for managing user-to-user follow relationships.
사용자 간 팔로우 관계를 관리하는 UserFollow 모델을 정의합니다.
"""
class UserFollow(Base):
    __tablename__ = 'users_follows_users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    # Foreign keys referencing the users involved in the follow relationship
    # 팔로우 관계에 포함된 사용자들을 참조하는 외래 키
    user_id = Column(ForeignKey('auth_user.id'))
    target_user_id = Column(ForeignKey('auth_user.id'))
    
    # Timestamps for creation and last update of the follow record
    # 팔로우 기록의 생성 및 마지막 수정 시간
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    # Relationship to the user initiating the follow
    # 팔로우를 시작한 사용자와의 관계
    user = relationship("User", backref="followings", foreign_keys=[user_id])

    # Relationship to the user being followed
    # 팔로우 대상 사용자와의 관계
    target_user = relationship("User", backref="followers", foreign_keys=[target_user_id])
