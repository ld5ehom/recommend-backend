from sqlalchemy import BigInteger, Column, Float, String, Time, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from src.core.database import Base
from src.models import restaurant_model, cuisine_type_model

# Mapping table between Restaurant and CuisineType
# Restaurant와 CuisineType 간 다대다 관계 매핑 테이블
class RestaurantCuisineType(Base):
    __tablename__ = 'restaurant_has_cuisine_types'

    # Foreign key to Restaurant table (composite primary key)
    # Restaurant 테이블의 외래 키 (복합 기본 키)
    restaurant_id = Column(ForeignKey('restaurants.id'), primary_key=True)

    # Foreign key to CuisineType table (composite primary key)
    # CuisineType 테이블의 외래 키 (복합 기본 키)
    cuisine_type_id = Column(ForeignKey('cuisine_types.id'), primary_key=True)

    # Relationship back to Restaurant
    # Restaurant과의 관계
    restaurant = relationship("Restaurant", back_populates="cuisine_types")

    # Relationship back to CuisineType
    # CuisineType과의 관계
    cuisine_type = relationship("CuisineType", back_populates="restaurants")
