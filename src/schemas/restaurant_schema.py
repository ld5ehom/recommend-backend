from datetime import datetime
from pydantic import BaseModel

from src.schemas import tag_schema, keyword_schema, cuisine_type_schema

"""
Represents a single tag associated with a restaurant.
레스토랑에 연결된 단일 태그 정보를 나타냅니다.
"""
class RestaurantTag(BaseModel):
    tag: tag_schema.TagSearchResultSimple

    class Config:
        from_attributes = True
        populate_by_name = True

"""
Represents a single keyword associated with a restaurant.
레스토랑에 연결된 단일 키워드 정보를 나타냅니다.
"""
class RestaurantKeyword(BaseModel):
    keyword: keyword_schema.KeywordSearchResultSimple

    class Config:
        from_attributes = True
        populate_by_name = True

"""
Represents a single cuisine type associated with a restaurant.
레스토랑에 연결된 단일 음식 유형 정보를 나타냅니다.
"""
class RestaurantCuisineType(BaseModel):
    cuisine_type: cuisine_type_schema.CuisineTypeSearchResultSimple

    class Config:
        from_attributes = True
        populate_by_name = True

"""
Base schema for common restaurant information.
레스토랑의 공통 정보를 정의하는 기본 스키마입니다.
"""
class RestaurantBase(BaseModel):
    name: str
    area_name: str | None = None
    address: str
    phone: str
    image_url: str | None = None

    start_time: datetime | None = None
    end_time: datetime | None = None
    last_order_time: datetime | None = None

    latitude: float | None = None
    longitude: float | None = None

    tags: list[RestaurantTag] | None = []
    keywords: list[RestaurantKeyword] | None = []
    cuisine_types: list[RestaurantCuisineType] | None = []

    class Config:
        from_attributes = True
        populate_by_name = True

"""
Full restaurant schema including ID and timestamps.
ID 및 생성/수정 시간이 포함된 전체 레스토랑 스키마입니다.
"""
class Restaurant(RestaurantBase):
    id: int
    updated_at: datetime
    created_at: datetime

"""
Schema for creating a restaurant entry.
레스토랑 생성 요청을 위한 스키마입니다.
"""
class RestaurantCreate(RestaurantBase):
    pass

"""
Schema for updating a restaurant entry.
레스토랑 수정 요청을 위한 스키마입니다.
"""
class RestaurantUpdate(RestaurantCreate):
    id: int
    updated_at: datetime

"""
Simple schema used for lightweight restaurant listings.
간단한 레스토랑 목록 조회에 사용되는 요약 스키마입니다.
"""
class RestaurantSearchResultSimple(RestaurantBase):
    id: int

"""
Detailed search result schema including tags, keywords, and cuisine types.
태그, 키워드, 음식 유형이 포함된 상세 검색 결과 스키마입니다.
"""
class RestaurantSearchResult(RestaurantSearchResultSimple):
    tags: list[RestaurantTag] | None = []
    keywords: list[RestaurantKeyword] | None = []
    cuisine_types: list[RestaurantCuisineType] | None = []
    updated_at: datetime
    created_at: datetime
