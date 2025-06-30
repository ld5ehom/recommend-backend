from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import BaseModel

from src.schemas import cuisine_type_category_schema

"""
Base schema for cuisine type creation and shared fields.
요리 종류 생성 및 공통 필드에 대한 기본 스키마입니다.
"""
class CuisineTypeBase(BaseModel):
    name: str

    class Config:
        from_attributes = True

"""
Full schema for a cuisine type including ID and timestamps.
ID 및 생성/수정 시간이 포함된 전체 요리 종류 스키마입니다.
"""
class CuisineType(CuisineTypeBase):
    id: int
    cuisine_type_category_id: int
    # restaurants: List[RestaurantSearchResultSimple] | None = None
    updated_at: datetime
    created_at: datetime

"""
Schema for creating a new cuisine type.
새로운 요리 종류 생성을 위한 요청 스키마입니다.
"""
class CuisineTypeCreate(CuisineTypeBase):
    cuisine_type_category_id: int

"""
Schema for updating an existing cuisine type.
기존 요리 종류를 수정하기 위한 요청 스키마입니다.
"""
class CuisineTypeUpdate(CuisineTypeCreate):
    id: int
    cuisine_type_category_id: int
    updated_at: datetime

"""
Compact schema for referencing or listing cuisine types.
간단한 참조 또는 목록 조회에 사용되는 요리 종류 요약 스키마입니다.
"""
class CuisineTypeSearchResultSimple(CuisineTypeBase):
    id: int
    cuisine_type_category_id: int

"""
Detailed cuisine type schema including category relation and timestamps.
카테고리 정보 및 생성/수정 시간이 포함된 상세 요리 종류 스키마입니다.
"""
class CuisineTypeSearchResult(CuisineTypeSearchResultSimple):
    cuisine_type_category: cuisine_type_category_schema.CuisineTypeCategorySearchResultSimple | None = None
    updated_at: datetime
    created_at: datetime
