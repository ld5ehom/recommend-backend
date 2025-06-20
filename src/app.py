from fastapi import FastAPI

from src.routers.index_router import router as index_router
from src.routers.users_router import router as users_router
from src.routers.articles_router import router as articles_router

"""
Creates the FastAPI app instance with custom title and OpenAPI tags.
FastAPI 인스턴스를 생성하고, 제목과 OpenAPI 태그 메타데이터를 설정합니다.
"""
app = FastAPI(
    title = "Store Management and Recommendation System API",
    # openapi_tags = tags_metadata
)

app.include_router(index_router)
app.include_router(users_router, prefix="/users")
app.include_router(articles_router, prefix="/articles")
