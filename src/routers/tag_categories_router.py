from fastapi import APIRouter, Depends

from src.schemas import tag_category_schema
from src.schemas import tag_schema
from src.services import tag_service

router = APIRouter(tags=["Tag Categories"])

# Retrieve all tag categories
# 모든 태그 카테고리 목록 조회
@router.get("/", 
            response_model=list[tag_category_schema.TagCategorySearchResult])
async def read_tag_categories(
    tag_categories: list[tag_category_schema.TagCategorySearchResult] = Depends(tag_service.get_tag_categories)
):
    return tag_categories

# Retrieve a specific tag category by ID
# 특정 태그 카테고리 ID로 조회
@router.get("/{id}", 
            response_model=tag_category_schema.TagCategory)
async def read_tag_category(
    tag_category: tag_category_schema.TagCategory = Depends(tag_service.get_tag_category_by_id)
):
    return tag_category

# Retrieve all tags under a specific tag category
# 특정 태그 카테고리에 속한 모든 태그 조회
@router.get("/{id}/tags", 
            response_model=list[tag_schema.TagSearchResultSimple])
async def read_tags_by_tag_category_id(
    tags: list[tag_schema.TagSearchResultSimple] = Depends(tag_service.get_tags_by_tag_category_id)
):
    return tags
