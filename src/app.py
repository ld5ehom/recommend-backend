from fastapi import FastAPI

from src.routers.index_router import router as index_router

"""
Creates the FastAPI app instance with custom title and OpenAPI tags.
FastAPI 인스턴스를 생성하고, 제목과 OpenAPI 태그 메타데이터를 설정합니다.
"""
app = FastAPI(
    title = "Store Recommendations System API",
    # openapi_tags = tags_metadata
)

app.include_router(index_router)
