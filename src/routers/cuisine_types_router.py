from fastapi import APIRouter, Depends
from src.schemas import cuisine_type_schema
from src.services import cuisine_type_service

router = APIRouter(tags=["Cuisine Types"])

# Retrieve all cuisine types
# 모든 음식 유형 목록 조회
@router.get("/", 
            response_model=list[cuisine_type_schema.CuisineTypeSearchResult])
async def read_cuisine_types(
    cuisine_types: list[cuisine_type_schema.CuisineTypeSearchResult] = Depends(cuisine_type_service.get_cuisine_types)
):
    return cuisine_types

# Retrieve a specific cuisine type by ID
# 특정 음식 유형 ID로 조회
@router.get("/{id}", response_model=cuisine_type_schema.CuisineType)
async def read_cuisine_type(
    cuisine_type: cuisine_type_schema.CuisineType = Depends(cuisine_type_service.get_cuisine_type_by_id)
):
    return cuisine_type
