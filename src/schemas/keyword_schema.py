from datetime import datetime
from typing import TYPE_CHECKING, List
from pydantic import BaseModel
from src.schemas import tag_category_schema

"""
Defines schema models for keyword data, including basic structure, creation/update models, and search result formats.
키워드 데이터를 위한 스키마 모델을 정의하며, 기본 구조, 생성/수정 모델, 검색 결과 형식을 포함합니다.
"""
class KeywordBase(BaseModel):
    name: str

    class Config:
        from_attributes = True



class Keyword(KeywordBase):
    id: int
    updated_at: datetime
    created_at: datetime

    # (Optional) Related restaurants can be added here if needed
    # (선택 사항) 필요 시 관련된 식당 정보를 여기에 추가 가능
    # restaurants: List[RestaurantSearchResultSimple] | None = None


class KeywordCreate(KeywordBase):
    # Schema for creating a new keyword
    # 새 키워드 생성을 위한 스키마
    pass


class KeywordUpdate(KeywordCreate):
    id: int
    updated_at: datetime

# Simple search result with ID
# ID를 포함한 간단한 검색 결과
class KeywordSearchResultSimple(KeywordBase):
    id: int


# Full search result including timestamps
# 타임스탬프를 포함한 전체 검색 결과
class KeywordSearchResult(KeywordSearchResultSimple):
    updated_at: datetime
    created_at: datetime
