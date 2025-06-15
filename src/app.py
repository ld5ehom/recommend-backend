from fastapi import FastAPI

from openapi_metadata import tags_metadata

"""
Creates the FastAPI app instance with custom title and OpenAPI tags.
FastAPI 인스턴스를 생성하고, 제목과 OpenAPI 태그 메타데이터를 설정합니다.
"""
app = FastAPI(
    title = "Product Recommendations System API",
    openapi_tags = tags_metadata
)
