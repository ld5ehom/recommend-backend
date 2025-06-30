import datetime

from sqlalchemy import BigInteger, String, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.core.database import Base
from src.models import restaurant_keyword_model

"""
Defines the Keyword model used for tagging restaurants with descriptive keywords.
식당에 키워드를 태깅하기 위한 Keyword 모델을 정의합니다.
"""
class Keyword(Base):
    __tablename__ = "keywords"

    # Unique identifier for the keyword
    # 키워드의 고유 식별자
    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)

    # Name of the keyword
    name = Column(String, nullable=False)

    # Timestamp of record creation
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    # Timestamp of last update
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    # Relationship to RestaurantKeyword association table
    # RestaurantKeyword 연관 테이블과의 관계 설정
    restaurants = relationship("RestaurantKeyword", back_populates="keyword")
