import datetime

from sqlalchemy import BigInteger, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from src.core.database import Base
from src.models import restaurant_cuisine_type_model

# CuisineType 테이블 모델 정의
# Defines the table model for CuisineType (요리 종류)
class CuisineType(Base):
    __tablename__ = "cuisine_types"

    # Primary key for the cuisine type
    # 요리 종류의 기본 키
    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)

    # Name of the cuisine type
    # 요리 종류 이름
    name = Column(String, nullable=False)
    
    # Foreign key linking to cuisine type category
    # 요리 종류 카테고리와의 외래 키 연결
    cuisine_type_category_id = Column(BigInteger, ForeignKey("cuisine_type_categories.id"))

    # Creation timestamp
    # 생성 시간
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    # Last update timestamp
    # 마지막 수정 시간
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    # Relationship to CuisineTypeCategory
    # 요리 종류 카테고리와의 관계
    cuisine_type_category = relationship("CuisineTypeCategory", back_populates="cuisine_types")

    # Relationship to RestaurantCuisineType mapping table
    # RestaurantCuisineType 매핑 테이블과의 관계
    restaurants = relationship("RestaurantCuisineType", back_populates="cuisine_type")


# CuisineTypeCategory 테이블 모델 정의
# Defines the table model for CuisineTypeCategory (요리 종류 카테고리)
class CuisineTypeCategory(Base):
    __tablename__ = "cuisine_type_categories"

    # Primary key for the cuisine type category
    # 요리 종류 카테고리의 기본 키
    id = Column(BigInteger, primary_key=True, autoincrement=True)

    # Name of the cuisine type category
    # 카테고리 이름
    name = Column(String, unique=True, index=True, nullable=False)
    
    # Creation timestamp
    # 생성 시간
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    # Last update timestamp
    # 마지막 수정 시간
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    # Relationship to associated cuisine types
    # 관련된 요리 종류들과의 관계
    cuisine_types = relationship("CuisineType", back_populates="cuisine_type_category")
