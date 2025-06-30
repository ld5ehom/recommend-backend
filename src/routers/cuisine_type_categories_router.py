from fastapi import APIRouter, Depends

from src.schemas import cuisine_type_category_schema
from src.schemas import cuisine_type_schema
from src.services import cuisine_type_service

router = APIRouter(tags=["Cuisine Type Categories"])

# Retrieve all cuisine type categories
# 모든 음식 유형 카테고리 목록 조회
@router.get("/", 
            response_model=list[cuisine_type_category_schema.CuisineTypeCategorySearchResult])
async def read_cuisine_type_categories(
    cuisine_type_categories: list[cuisine_type_category_schema.CuisineTypeCategorySearchResult] = Depends(
        cuisine_type_service.get_cuisine_type_categories
    )
):
    return cuisine_type_categories

# Retrieve a specific cuisine type category by ID
# 특정 음식 유형 카테고리 ID로 조회
@router.get("/{id}", 
            response_model=cuisine_type_category_schema.CuisineTypeCategory)
async def read_cuisine_type_category(
    cuisine_type_category: cuisine_type_category_schema.CuisineTypeCategory = Depends(
        cuisine_type_service.get_cuisine_type_category_by_id
    )
):
    return cuisine_type_category

# Retrieve cuisine types under a specific cuisine type category
# 특정 음식 유형 카테고리에 속한 음식 유형들 조회
@router.get("/{id}/tags", 
            response_model=list[cuisine_type_schema.CuisineTypeSearchResultSimple])
async def read_cuisine_types_by_cuisine_type_category_id(
    cuisine_types: list[cuisine_type_schema.CuisineTypeSearchResultSimple] = Depends(
        cuisine_type_service.get_cuisine_types_by_cuisine_type_category_id
    )
):
    return cuisine_types
