from enum import Enum
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from src.models import cuisine_type_model, restaurant_model
from src.dependencies.database import get_db


# Enum to specify ordering fields for CuisineType
# 음식 유형 정렬 기준 열 정의
class CuisineTypeOrderBy(str, Enum):
    name = "name"
    cuisine_type_category_id = "cuisine_type_category_id"
    created_at = "created_at"
    updated_at = "updated_at"

# Enum to specify ordering fields for CuisineTypeCategory
# 음식 유형 카테고리 정렬 기준 열 정의
class CuisineTypeCategoryOrderBy(str, Enum):
    name = "name"
    created_at = "created_at"
    updated_at = "updated_at"

# Enum for ascending/descending sort
# 오름차순/내림차순 정렬 기준
class Sort(str, Enum):
    asc = "asc"
    desc = "desc"


# Retrieve a CuisineType by ID
# ID로 특정 음식 유형 조회
def get_cuisine_type_by_id(id: int, db: Session = Depends(get_db)):
    cuisine_type = db.query(cuisine_type_model.CuisineType).filter(cuisine_type_model.CuisineType.id == id).first()
    if not cuisine_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return cuisine_type


# Retrieve a CuisineTypeCategory by ID
# ID로 음식 유형 카테고리 조회
def get_cuisine_type_category_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(cuisine_type_model.CuisineTypeCategory).filter(cuisine_type_model.CuisineTypeCategory.id == id).first()


# Retrieve all CuisineTypes, optionally filtered by restaurant_id
# 전체 음식 유형 조회 (restaurant_id 기준 필터링 가능)
def get_cuisine_types(
    restaurant_id: int = None,
    skip: int = 0,
    limit: int = 100,
    order_by: CuisineTypeOrderBy = CuisineTypeOrderBy.updated_at,
    sort: Sort = Sort.desc,
    db: Session = Depends(get_db)
):
    include_ids = []

    if restaurant_id:
        restaurant = db.query(restaurant_model.Restaurant).filter(restaurant_model.Restaurant.id == restaurant_id).first()
        for c in restaurant.cuisine_types:
            include_ids.append(c.cuisine_type.id)
        include_ids = list(dict.fromkeys(include_ids))  # Remove duplicates

    if include_ids:
        cuisine_types = db.query(cuisine_type_model.CuisineType).filter(
            cuisine_type_model.CuisineType.id.in_(include_ids)
        ).order_by(text(f"{order_by.value} {sort.value}")).offset(skip).limit(limit).all()
    else:
        cuisine_types = db.query(cuisine_type_model.CuisineType).order_by(
            text(f"{order_by.value} {sort.value}")
        ).offset(skip).limit(limit).all()

    return cuisine_types


# Retrieve all CuisineTypes under a specific CuisineTypeCategory
# 특정 음식 유형 카테고리에 속한 모든 음식 유형 조회
def get_cuisine_types_by_cuisine_type_category_id(
    id: int,
    skip: int = 0,
    limit: int = 100,
    order_by: CuisineTypeOrderBy = CuisineTypeOrderBy.updated_at,
    sort: Sort = Sort.desc,
    db: Session = Depends(get_db)
):
    return db.query(cuisine_type_model.CuisineType).filter(
        cuisine_type_model.CuisineType.cuisine_type_category_id == id
    ).order_by(text(f"{order_by.value} {sort.value}")).offset(skip).limit(limit).all()


# Retrieve all CuisineTypeCategories with optional pagination and sorting
# 전체 음식 유형 카테고리 목록 조회 (페이지네이션 및 정렬 가능)
def get_cuisine_type_categories(
    skip: int = 0,
    limit: int = 100,
    order_by: CuisineTypeCategoryOrderBy = CuisineTypeCategoryOrderBy.updated_at,
    sort: Sort = Sort.desc,
    db: Session = Depends(get_db)
):
    return db.query(cuisine_type_model.CuisineTypeCategory).order_by(
        text(f"{order_by.value} {sort.value}")
    ).offset(skip).limit(limit).all()
