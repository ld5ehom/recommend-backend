from sqlalchemy import BigInteger, Column, Float, String, Time, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from src.core.database import Base
from src.models import restaurant_model, keyword_model

"""
Defines the association table for the many-to-many relationship between restaurants and keywords.
식당과 키워드 간의 다대다 관계를 위한 연결 테이블을 정의합니다.
"""
class RestaurantKeyword(Base):
    __tablename__ = 'restaurant_has_keywords'

    # Foreign key referencing Restaurant ID, part of composite primary key
    # 식당 ID를 참조하는 외래 키 (복합 기본 키 구성 요소)
    restaurant_id = Column(ForeignKey('restaurants.id'), primary_key=True)

    # Foreign key referencing Keyword ID, part of composite primary key
    # 키워드 ID를 참조하는 외래 키 (복합 기본 키 구성 요소)
    keyword_id = Column(ForeignKey('keywords.id'), primary_key=True)

    # Relationship to the Restaurant model
    # Restaurant 모델과의 관계 설정
    restaurant = relationship("Restaurant", back_populates="keywords")

    # Relationship to the Keyword model
    # Keyword 모델과의 관계 설정
    keyword = relationship("Keyword", back_populates="restaurants")
