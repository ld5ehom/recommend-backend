from fastapi import APIRouter, Depends

from src.schemas import article_schema
from src.services import article_service

"""
Defines API endpoints for retrieving articles, including listing all articles and fetching a specific article by ID.
기사 목록 조회 및 특정 기사 조회를 위한 API 엔드포인트를 정의합니다.
"""
router = APIRouter(tags=["Articles"])

# Retrieve a list of all articles
# 전체 기사 목록을 조회합니다.
@router.get("/", 
            response_model=list[article_schema.Article])
async def read_articles(articles: list[article_schema.Article] = Depends(article_service.get_articles)):
    return articles

# Retrieve a specific article by its ID
# 특정 ID를 가진 기사를 조회합니다.
@router.get("/{id}", 
            response_model=article_schema.Article)
async def read_article(article: article_schema.Article = Depends(article_service.get_article_by_id)):
    return article
