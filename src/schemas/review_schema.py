from datetime import datetime
from pydantic import BaseModel
from src.schemas import restaurant_schema

# Base schema for Review
# 리뷰 기본 스키마
class ReviewBase(BaseModel):
    title: str
    rating: int
    content: str
    author: str

    class Config:
        from_attributes = True

# Full schema for Review with all fields
# 전체 리뷰 스키마 (조회용)
class Review(ReviewBase):
    id: int
    restaurant_id: int
    restaurant: restaurant_schema.RestaurantSearchResultSimple | None = None
    updated_at: datetime
    created_at: datetime

# Schema for creating a review
# 리뷰 생성 스키마
class ReviewCreate(ReviewBase):
    restaurant_id: int

# Schema for updating a review
# 리뷰 수정 스키마
class ReviewUpdate(ReviewCreate):
    id: int
    restaurant_id: int
    updated_at: datetime

# Simple schema for search result listing
# 간단한 리뷰 검색 결과 스키마
class ReviewSearchResultSimple(ReviewBase):
    id: int

# Extended search result schema with relations and timestamps
# 상세 리뷰 검색 결과 스키마
class ReviewSearchResult(ReviewSearchResultSimple):
    restaurant: restaurant_schema.RestaurantSearchResultSimple | None = None
    updated_at: datetime
    created_at: datetime
