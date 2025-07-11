import requests
from datetime import datetime, timedelta

from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.weather import (
    DATA_GO_KR_API_KEY_DECODED,
    DATA_GO_KR_API_KEY_ENCODED,
    DATA_GO_KR_API_URL_USN,
    DATA_GO_KR_API_URL_WDL,
)
from src.dependencies.map import get_grid_by_coordinate
from src.dependencies.database import get_db


def get_ultra_srt_ncst_by_coordinate(
    longitude: float = -118.2437, latitude: float = 34.0522, format: str = "json"
):
    # Fetch ultra short-term forecast data from weather API
    # 기상청 초단기 실황 API를 호출하여 날씨 데이터를 조회합니다

    grid_x, grid_y = get_grid_by_coordinate(latitude, longitude)

    base_time = datetime.now() - timedelta(hours=1)  # Account for update delay
    # API 응답 지연을 고려하여 현재 시간에서 1시간을 뺀 기준시간 사용

    apiurl = DATA_GO_KR_API_URL_USN
    params = {
        "serviceKey": DATA_GO_KR_API_KEY_DECODED,
        "pageNo": "1",
        "numOfRows": "1000",
        "dataType": "JSON",
        "base_date": datetime.now().strftime("%Y%m%d"),
        "base_time": base_time.strftime("%H00"),
        "nx": grid_x,
        "ny": grid_y,
    }

    response = requests.get(apiurl, params=params)
    print(response.url)  # For debugging purposes / 디버깅용

    return response.json()


def get_wthr_data_list_by_coordinate(
    longitude: float = -118.2437,
    latitude: float = 34.0522,
    format: str = "json",
    db: Session = Depends(get_db),
):
    # Fetch historical weather observation data from the nearest station
    # 가장 가까운 관측소로부터 과거 관측 데이터를 조회합니다

    query = """
        SELECT 
            id, 
            os_id, 
            ( 6371 * acos(
                cos(radians(%s)) * cos(radians(latitude)) *
                cos(radians(longitude) - radians(%s)) +
                sin(radians(%s)) * sin(radians(latitude))
            )) AS distance,
            latitude, longitude
        FROM observation_stations
        WHERE is_usable = 1
        HAVING distance < 25
        ORDER BY distance
        LIMIT 1;
    """ % (latitude, longitude, latitude)

    result = db.execute(text(query))
    nearest_observation_station = [r for r in result][0]

    baseDate = datetime.now() - timedelta(days=1)

    apiurl = DATA_GO_KR_API_URL_WDL
    params = {
        "serviceKey": DATA_GO_KR_API_KEY_DECODED,
        "pageNo": "1",
        "numOfRows": "10",
        "dataType": format,
        "dataCd": "ASOS",
        "dateCd": "HR",
        "startDt": baseDate.strftime("%Y%m%d"),
        "startHh": (datetime.now() - timedelta(hours=1)).strftime("%H"),
        "endDt": baseDate.strftime("%Y%m%d"),
        "endHh": datetime.now().strftime("%H"),
        "stnIds": nearest_observation_station[1],
    }

    response = requests.get(apiurl, params=params)
    print(response.url)  # For debugging / 디버깅용 출력

    return response.json()
