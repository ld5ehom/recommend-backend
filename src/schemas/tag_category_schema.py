from datetime import datetime
from pydantic import BaseModel

"""
Defines base schema for tag category data.
태그 카테고리 데이터의 기본 스키마를 정의합니다.
"""
class TagCategoryBase(BaseModel):
    # Name of the tag category
    # 태그 카테고리 이름
    name: str

    class Config:
        from_attributes = True

"""
Represents a complete tag category with ID and timestamps.
ID 및 타임스탬프를 포함한 전체 태그 카테고리 정보를 나타냅니다.
"""
class TagCategory(TagCategoryBase):
    id: int
    updated_at: datetime
    created_at: datetime

"""
Schema for creating a new tag category.
새로운 태그 카테고리를 생성할 때 사용하는 스키마입니다.
"""
class TagCategoryCreate(TagCategoryBase):
    pass

"""
Schema for updating an existing tag category.
기존 태그 카테고리를 수정할 때 사용하는 스키마입니다.
"""
class TagCategoryUpdate(TagCategoryCreate):
    id: int
    updated_at: datetime

"""
Simplified search result schema for tag category.
간략한 태그 카테고리 검색 결과를 위한 스키마입니다.
"""
class TagCategorySearchResultSimple(TagCategoryBase):
    id: int

"""
Detailed search result schema including timestamps.
타임스탬프를 포함한 상세 검색 결과 스키마입니다.
"""
class TagCategorySearchResult(TagCategorySearchResultSimple):
    updated_at: datetime
    created_at: datetime
