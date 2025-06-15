from sqlalchemy import BigInteger, Column, Float, String, Time, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from src.core.database import Base
from src.models import restaurant_tag_model

"""
Defines the SQLAlchemy model for restaurants, including metadata such as address,
contact information, location, and relations to other entities like tags, cuisine types, and reviews.
레스토랑의 주소, 연락처, 위치 등의 메타데이터와 태그, 요리유형, 리뷰 등 다른 엔티티와의 관계를 포함한 SQLAlchemy 모델을 정의합니다.
"""

# Restaurant model storing metadata and relationships for each store
# 각 음식점의 메타데이터 및 관련 관계 정보를 저장하는 레스토랑 모델
class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)

    name = Column(String, nullable=False)
    area_name = Column(String, nullable=True)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    image_url = Column(String, nullable=True)

    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)
    last_order_time = Column(Time, nullable=True)

    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    updated_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False)

    tags = relationship("RestaruantTag", back_populates="restaurant")
    cuisine_types = relationship("RestaruantCuisineType", back_populates="restaurant")
    keywords = relationship("RestaruantKeyword", back_populates="restaurant")
    reviews = relationship("Review", back_populates="restaurant")
    blog_reviews = relationship("BlogReview", back_populates="restaurant")
    like_users = relationship("UserLike", back_populates="restaurant")
