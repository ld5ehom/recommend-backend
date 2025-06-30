from datetime import datetime
from pydantic import BaseModel
from src.schemas import restaurant_schema

"""
Defines schema models for blog review data transfer, including base attributes, creation/update, and search results.
블로그 리뷰 데이터 전달을 위한 스키마 모델을 정의하며, 기본 속성, 생성/수정, 검색 결과를 포함합니다.
"""
class BlogReviewBase(BaseModel):
    title: str
    published_date: datetime
    blog_url: str

    class Config:
        from_attributes = True


class BlogReview(BlogReviewBase):
    id: int
    restaurant_id: int

    # Optional nested restaurant summary
    # 선택적인 식당 요약 정보
    restaurant: restaurant_schema.RestaurantSearchResultSimple | None = None

    updated_at: datetime
    created_at: datetime


class BlogReviewCreate(BlogReviewBase):
    # Restaurant ID for which the review is created
    # 리뷰가 작성될 식당의 ID
    restaurant_id: int
    pass


class BlogReviewUpdate(BlogReviewBase):
    id: int
    restaurant_id: int
    updated_at: datetime


class BlogReviewSearchResultSimple(BlogReviewBase):
    id: int
    restaurant_id: int


class BlogReviewSearchResult(BlogReviewSearchResultSimple):
    # Optional nested restaurant data
    # 선택적인 식당 데이터
    restaurant: restaurant_schema.RestaurantSearchResultSimple | None = None

    # Update timestamp
    updated_at: datetime

    # Creation timestamp
    created_at: datetime
