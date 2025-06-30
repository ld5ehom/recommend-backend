from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import BaseModel

from src.schemas import tag_category_schema

"""
Base schema for tag creation and shared tag fields.
태그 생성 및 공통 필드에 대한 기본 스키마입니다.
"""
class TagBase(BaseModel):
    name: str

    class Config:
        from_attributes = True
        populate_by_name = True

"""
Full tag schema including ID and timestamps.
ID와 생성/수정 시간이 포함된 전체 태그 스키마입니다.
"""
class Tag(TagBase):
    id: int
    tag_category_id: int
    # restaurants: List[RestaurantSearchResultSimple] | None = None
    updated_at: datetime
    created_at: datetime

"""
Schema for creating a new tag.
새로운 태그 생성을 위한 요청 스키마입니다.
"""
class TagCreate(TagBase):
    tag_category_id: int

"""
Schema for updating an existing tag.
기존 태그를 수정하기 위한 요청 스키마입니다.
"""
class TagUpdate(TagCreate):
    id: int
    tag_category_id: int
    updated_at: datetime

"""
Compact schema for listing or referencing a tag.
간단한 조회 또는 참조에 사용되는 요약 태그 스키마입니다.
"""
class TagSearchResultSimple(TagBase):
    id: int
    tag_category_id: int

"""
Detailed tag schema including its category and timestamps.
태그의 카테고리 정보와 생성/수정 시간을 포함한 상세 스키마입니다.
"""
class TagSearchResult(TagSearchResultSimple):
    tag_category: tag_category_schema.TagCategorySearchResultSimple | None = None
    updated_at: datetime
    created_at: datetime
