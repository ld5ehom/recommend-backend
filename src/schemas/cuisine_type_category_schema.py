from datetime import datetime
from pydantic import BaseModel

"""
Base schema for cuisine type categories with a name field.
요리 종류 카테고리의 이름 필드를 포함한 기본 스키마입니다.
"""
class CuisineTypeCategoryBase(BaseModel):
    name: str

    class Config:
        from_attributes = True

"""
Full schema for a cuisine type category with ID and timestamps.
ID 및 생성/수정 시간이 포함된 전체 요리 종류 카테고리 스키마입니다.
"""
class CuisineTypeCategory(CuisineTypeCategoryBase):
    id: int
    updated_at: datetime
    created_at: datetime

"""
Schema for creating a new cuisine type category.
새로운 요리 종류 카테고리를 생성하기 위한 요청 스키마입니다.
"""
class CuisineTypeCategoryCreate(CuisineTypeCategoryBase):
    pass

"""
Schema for updating an existing cuisine type category.
기존 요리 종류 카테고리를 수정하기 위한 요청 스키마입니다.
"""
class CuisineTypeCategoryUpdate(CuisineTypeCategoryCreate):
    id: int
    updated_at: datetime

"""
Compact schema for referencing cuisine type categories.
간단한 참조 또는 목록 조회에 사용되는 요리 종류 카테고리 요약 스키마입니다.
"""
class CuisineTypeCategorySearchResultSimple(CuisineTypeCategoryBase):
    id: int

"""
Detailed schema for cuisine type categories including timestamps.
생성/수정 시간이 포함된 상세 요리 종류 카테고리 스키마입니다.
"""
class CuisineTypeCategorySearchResult(CuisineTypeCategorySearchResultSimple):
    # tags: List[TagSearchResultSimple] | None = None
    updated_at: datetime
    created_at: datetime
