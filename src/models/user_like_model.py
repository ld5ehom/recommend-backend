import datetime
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base
from src.models import restaurant_model, user_model

"""
Defines the UserLike model to manage the relationship between users and liked restaurants.
사용자와 선호하는 음식점 간의 관계를 관리하는 UserLike 모델을 정의합니다.
"""
class UserLike(Base):
    __tablename__ = 'users_likes_restaurants'

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    # Foreign keys referencing the user and the liked restaurant
    # 사용자와 좋아요를 누른 음식점을 참조하는 외래 키
    user_id = Column(ForeignKey('auth_user.id'))
    restaurant_id = Column(ForeignKey('restaurants.id'))

    # Timestamps for creation and last update of the like record
    # 좋아요 기록의 생성 및 마지막 수정 시간
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    
    # Relationship to the liking user
    # 좋아요를 누른 사용자와의 관계
    user = relationship("User", back_populates="like_restaurants")

    # Relationship to the liked restaurant
    # 좋아요 대상 음식점과의 관계
    restaurant = relationship("Restaurant", back_populates="like_users")
