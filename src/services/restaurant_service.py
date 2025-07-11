from enum import Enum
from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import text

from src.models import restaurant_model, tag_model, restaurant_tag_model, cuisine_type_model
from src.services import tag_service  
from src.dependencies.database import get_db

from src.dependencies.predict import predict_cuisine_type_by_weather
from src.dependencies.weather import get_wthr_data_list_by_coordinate

class RestaurantOrderBy(str, Enum):
    name = "name"
    created_at = "created_at"
    updated_at = "updated_at"

class Sort(str, Enum):
    asc = "asc"
    desc = "desc"

# Get restaurant by ID
def get_restaurant_by_id(id: int, db: Session = Depends(get_db)):
    restaurant = db.query(restaurant_model.Restaurant).filter(restaurant_model.Restaurant.id == id).first()
    if not restaurant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return restaurant

# Get restaurants based on multiple filters including location and weather
# 위치와 날씨 정보를 포함한 다양한 조건으로 식당을 조회합니다.
def get_restaurants(tags: str | None=None, 
                    cuisine_type_categories: str | None=None, 
                    cuisine_types: str | None=None, 
                    area: str | None=None, 
                    longitude: float | None=None, 
                    latitude: float | None=None, 
                    distance: float | None=None,
                    skip: int = 0, 
                    limit: int = 100, 
                    order_by: RestaurantOrderBy = RestaurantOrderBy.updated_at, 
                    sort: Sort = Sort.desc, 
                    db: Session = Depends(get_db)):

    include_ids_by_coordinate = []

    # If location and distance are provided, search nearby restaurants and get weather info
    # 위치 정보가 제공되면 반경 내 식당을 조회하고 날씨 데이터를 가져옵니다.
    if longitude and latitude and distance:
        query = f"""
            SELECT 
                id,
                ( 6371 * acos( cos( radians({latitude}) ) * cos( radians(latitude ) ) * cos( radians( longitude ) - radians({longitude}) ) + sin( radians({latitude}) ) * sin( radians( latitude ) ) ) ) AS distance,
                latitude, longitude
            FROM restaurants
            HAVING distance < {distance}
            ORDER BY distance;
        """
        result = db.execute(text(query))
        include_ids_by_coordinate = [r[0] for r in result]
        include_ids_by_coordinate = list(dict.fromkeys(include_ids_by_coordinate))

        weather_info = get_wthr_data_list_by_coordinate(longitude, latitude, "json", db)
        weather = weather_info['response']['body']['items']['item'][0]

        temperature = float(weather.get('ta', 0.0) or 0.0)
        precipitation = float(weather.get('dsnw', 0.0) or 0.0)
        cloudiness = float(weather.get('dc10Tca', 0.0) or 0.0)
        snowfall = float(weather.get('dsnw', 0.0) or 0.0)
        pressure = float(weather.get('pa', 0.0) or 0.0)

        prediction = predict_cuisine_type_by_weather(temperature, precipitation, cloudiness, snowfall, pressure)
        predicted_types = ",".join(prediction.keys())
        cuisine_types = (cuisine_types + "," + predicted_types) if cuisine_types else predicted_types

    include_ids_by_tags = []

    # Filter by tag
    if tags:
        tag_list = tags.split(',')
        tags = db.query(tag_model.Tag).filter(tag_model.Tag.name.in_(tag_list)).all()
        for t in tags:
            for r in t.restaurants:
                include_ids_by_tags.append(r.restaurant_id)
        include_ids_by_tags = list(dict.fromkeys(include_ids_by_tags))

    include_ids_by_cuisine_type_categories = []

    # Filter by cuisine type category
    if cuisine_type_categories:
        category_list = cuisine_type_categories.split(',')
        cuisine_type_categories = db.query(cuisine_type_model.CuisineTypeCategory).filter(
            cuisine_type_model.CuisineTypeCategory.name.in_(category_list)).all()

        for cc in cuisine_type_categories:
            for c in cc.cuisine_types:
                for r in c.restaurants:
                    include_ids_by_cuisine_type_categories.append(r.restaurant_id)
        include_ids_by_cuisine_type_categories = list(dict.fromkeys(include_ids_by_cuisine_type_categories))

    include_ids_by_cuisine_types = []

    # Filter by cuisine types
    if cuisine_types:
        cuisine_type_list = cuisine_types.split(',')
        cuisine_types = db.query(cuisine_type_model.CuisineType).filter(
            cuisine_type_model.CuisineType.name.in_(cuisine_type_list)).all()

        for c in cuisine_types:
            for r in c.restaurants:
                include_ids_by_cuisine_types.append(r.restaurant_id)
        include_ids_by_cuisine_types = list(dict.fromkeys(include_ids_by_cuisine_types))

    include_ids_by_area = []

    # Filter by area string in address
    if area:
        restaurants = db.query(restaurant_model.Restaurant).filter(
            restaurant_model.Restaurant.address.ilike(f'%{area}%')).all()

        for r in restaurants:
            include_ids_by_area.append(r.id)
        include_ids_by_area = list(dict.fromkeys(include_ids_by_area))

    # Merge all matching restaurant IDs from filters
    include_ids = (
        include_ids_by_tags +
        include_ids_by_cuisine_type_categories +
        include_ids_by_area +
        include_ids_by_coordinate +
        include_ids_by_cuisine_types
    )
    include_ids = list(dict.fromkeys(include_ids))

    # Query restaurants using filters and sorting
    # 필터와 정렬 조건에 맞게 식당 데이터를 조회합니다.
    if include_ids:
        restaurants = db.query(restaurant_model.Restaurant)\
            .filter(restaurant_model.Restaurant.id.in_(include_ids))\
            .order_by(text(f"{order_by.value} {sort.value}"))\
            .offset(skip)\
            .limit(limit)\
            .all()
    else:
        restaurants = db.query(restaurant_model.Restaurant)\
            .order_by(text(f"{order_by.value} {sort.value}"))\
            .offset(skip)\
            .limit(limit)\
            .all()

    return restaurants
