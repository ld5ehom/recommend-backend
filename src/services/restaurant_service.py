from enum import Enum

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from src.models import (
    restaurant_model,
    tag_model, 
    cuisine_type_model
)
from src.dependencies.database import get_db


class RestaurantOrderBy(str, Enum):
    name = "name"
    created_at = "created_at"
    updated_at = "updated_at"

class Sort(str, Enum):
    asc = "asc"
    desc = "desc"


# Get a restaurant by its ID
# 식당 ID로 단일 식당 조회
def get_restaurant_by_id(id: int, db: Session = Depends(get_db)):
    restaurant = db.query(restaurant_model.Restaurant).filter(restaurant_model.Restaurant.id == id).first()
    if not restaurant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return restaurant


# Get list of restaurants with optional filtering
# 다양한 필터(태그, 카테고리, 위치 등) 기반 식당 목록 조회
def get_restaurants(
    tags: str | None = None,
    cuisine_type_categories: str | None = None,
    cuisine_types: str | None = None,
    area: str | None = None,
    skip: int = 0,
    limit: int = 100,
    order_by: RestaurantOrderBy = RestaurantOrderBy.updated_at,
    sort: Sort = Sort.desc,
    db: Session = Depends(get_db)
):
    include_ids_by_tags = []

    if tags and tags != "":
        tag_list = tags.split(',')
        tags = db.query(tag_model.Tag).filter(tag_model.Tag.name.in_(tag_list)).all()

        for t in tags:
            for r in t.restaurants:
                include_ids_by_tags.append(r.restaurant_id)
        
        # 중복제거 
        include_ids_by_tags = list(dict.fromkeys(include_ids_by_tags))
       
    # 카테고리
    include_ids_by_cuisine_type_categories = []
    if cuisine_type_categories and cuisine_type_categories != "":
        cuisine_type_category_list = cuisine_type_categories.split(',')
        cuisine_type_categories = db.query(cuisine_type_model.CuisineTypeCategory).filter(cuisine_type_model.CuisineTypeCategory.name.in_(cuisine_type_category_list)).all()

        for cc in cuisine_type_categories:
            for c in cc.cuisine_types:
                for c in c.restaurants:
                    include_ids_by_cuisine_type_categories.append(c.restaurant_id)

        # 중복제거
        include_ids_by_cuisine_type_categories = list(dict.fromkeys(include_ids_by_cuisine_type_categories))

    # Area
    include_ids_by_area = []
    if area and area != "":
        restaurants = db.query(restaurant_model.Restaurant).filter(restaurant_model.Restaurant.address.ilike('%%%s%%' % area)).all()

        for r in restaurants:
            include_ids_by_area.append(r.id)

        include_ids_by_area = list(dict.fromkeys(include_ids_by_area))

    # 합치기
    include_ids = include_ids_by_tags + include_ids_by_cuisine_type_categories + include_ids_by_area 
    include_ids = list(dict.fromkeys(include_ids))


    if include_ids:
        restaurants = db.query(restaurant_model.Restaurant).filter(restaurant_model.Restaurant.id.in_(include_ids)).order_by(text("%s %s" % (order_by.value, sort.value))).offset(offset=skip).limit(limit=limit).all()
    else : 
        restaurants = db.query(restaurant_model.Restaurant).order_by(text("%s %s" % (order_by.value, sort.value))).offset(offset=skip).limit(limit=limit).all()

    return restaurants
