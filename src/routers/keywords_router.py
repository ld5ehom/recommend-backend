from fastapi import APIRouter, Depends
from src.schemas import keyword_schema
from src.services import keyword_service

"""
Provides API endpoints to retrieve keyword information.
키워드 정보를 조회하는 API 엔드포인트를 제공합니다.
"""
router = APIRouter(tags=["Keywords"])

# Retrieve a list of all keywords
# 모든 키워드 목록을 조회합니다.
@router.get("/", 
            response_model=list[keyword_schema.Keyword])
async def read_keywords(
    keywords: list[keyword_schema.Keyword] = Depends(keyword_service.get_keywords)
    ):
    return keywords

# Retrieve a specific keyword by ID
# 특정 ID로 키워드를 조회합니다.
@router.get("/{id}", 
            response_model=keyword_schema.Keyword)
async def read_keyword(
    keyword: keyword_schema.Keyword = Depends(keyword_service.get_keyword_by_id)
    ):
    return keyword
