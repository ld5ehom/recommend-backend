from fastapi import APIRouter, Depends

from src.schemas import (
    restaurant_schema,
    tag_schema,
    cuisine_type_schema
)
from src.services import (
    restaurant_service,
    tag_service,
    cuisine_type_service
)

router = APIRouter(tags=["Restaurants"])

# Retrieve a list of restaurants
# 식당 목록 조회
@router.get("/", 
            response_model=list[restaurant_schema.RestaurantSearchResult])
async def read_restaurants(
    restaurants: list[restaurant_schema.RestaurantSearchResult] = Depends(restaurant_service.get_restaurants)
):
    return restaurants

# Retrieve a single restaurant by ID
# 식당 상세 조회
@router.get("/{id}", 
            response_model=restaurant_schema.Restaurant)
async def read_restaurant(
    restaurant: restaurant_schema.Restaurant = Depends(restaurant_service.get_restaurant_by_id)
):
    return restaurant

# Retrieve cuisine types related to a restaurant
# 식당 관련 요리 타입 조회
@router.get("/{id}/cuisine_types", 
            response_model=list[cuisine_type_schema.CuisineTypeSearchResult])
async def read_cuisine_types_by_restaurant_id(
    cuisine_types: list[cuisine_type_schema.CuisineTypeSearchResult] = Depends(cuisine_type_service.get_cuisine_types)
):
    return cuisine_types

# Retrieve users who liked the restaurant
# 식당을 좋아요한 사용자 목록 조회 (미구현)
@router.get("/{id}/likers")
async def read_likers_by_restaurant_id(id: int):
    return {"system": True}

# Retrieve reviews of the restaurant
# 식당 리뷰 목록 조회 (미구현)
@router.get("/{id}/reviews")
async def read_reviews_by_restaurant_id(id: int):
    return {"system": True}

# Retrieve blog reviews of the restaurant
# 식당 블로그 리뷰 목록 조회 (미구현)
@router.get("/{id}/blog_reviews")
async def read_blog_reviews_by_restaurant_id(id: int):
    return {"system": True}

# Retrieve keywords related to the restaurant
# 식당 관련 키워드 조회 (미구현)
@router.get("/{id}/keywords")
async def read_keywords_by_restaurant_id(id: int):
    return {"system": True}

# Retrieve tags related to the restaurant
# 식당 관련 태그 조회 (미구현)
@router.get("/{id}/tags")
async def read_tags_by_restaurant_id(id: int):
    return {"system": True}
