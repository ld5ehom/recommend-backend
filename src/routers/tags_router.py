from fastapi import APIRouter, Depends

from src.schemas import tag_schema
from src.services import tag_service

router = APIRouter(tags=["Tags"])

# Retrieve all tags
# 모든 태그 목록 조회
@router.get("/", 
            response_model=list[tag_schema.TagSearchResult])
async def read_tags(
    tags: list[tag_schema.TagSearchResult] = Depends(tag_service.get_tags)
):
    return tags

# Retrieve a specific tag by ID
# 특정 태그 ID로 조회
@router.get("/{id}", 
            response_model=tag_schema.Tag)
async def read_tag(
    tag: tag_schema.Tag = Depends(tag_service.get_tag_by_id)
):
    return tag
