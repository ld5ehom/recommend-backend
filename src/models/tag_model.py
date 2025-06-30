import datetime

from sqlalchemy import BigInteger, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from src.core.database import Base
from src.models import restaurant_tag_model

"""
Defines SQLAlchemy models for tags and their categories.
태그 및 태그 카테고리를 위한 SQLAlchemy 모델을 정의합니다.
"""
# Tag model for individual tag entities
# 개별 태그 정보를 나타내는 모델
class Tag(Base):
    __tablename__ = "tags"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, index=True, nullable=False)

    tag_category_id = Column(BigInteger, ForeignKey("tag_categories.id"))

    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    tag_category = relationship("TagCategory", back_populates="tags")
    restaurants = relationship("RestaurantTag", back_populates="tag")

# TagCategory model for grouping tags under a category
# 태그들을 카테고리로 분류하기 위한 태그 카테고리 모델
class TagCategory(Base):
    __tablename__ = "tag_categories"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, index=True, nullable=False)

    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    tags = relationship("Tag", back_populates="tag_category")
