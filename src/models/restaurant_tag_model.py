from sqlalchemy import BigInteger, Column, Float, String, Time, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from src.core.database import Base
from src.models import restaurant_model, tag_model

"""
Defines the association table between restaurants and tags.
Each row connects a restaurant to one tag, allowing many-to-many relationships.
레스토랑과 태그 간의 연결 테이블을 정의합니다.
각 행은 하나의 레스토랑과 하나의 태그를 연결하여 다대다 관계를 가능하게 합니다.
"""

# Association table linking Restaurant and Tag in many-to-many relationship
# 다대다 관계를 위한 Restaurant와 Tag 간의 연결 테이블
class RestaurantTag(Base):
    __tablename__ = 'restaurant_has_tags'

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    restaurant_id = Column(ForeignKey('restaurants.id'), primary_key=True)
    tag_id = Column(ForeignKey('tags.id'), primary_key=True)

    restaurant = relationship("Restaurant", back_populates="tags")
    tag = relationship("Tag", back_populates="restaurants")
