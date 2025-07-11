import requests

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.dependencies.map import get_coordinate_by_address, get_address_by_coordinate
from src.dependencies.weather import get_ultra_srt_ncst_by_coordinate, get_wthr_data_list_by_coordinate
from src.dependencies.naver_serach_keywords import get_naver_search_keywords
from src.dependencies.predict import predict_cuisine_type_by_weather

from src.schemas import utility_schema
from src.services import utility_service  

router = APIRouter(tags=["Utilities"])

# Get coordinate (longitude, latitude) from a given address
# 주소로부터 좌표(경도, 위도)를 조회합니다
@router.get("/get_coordinate_by_address")
async def read_coordinate_by_address(address: str):
    response = get_coordinate_by_address(address)
    return response

# Get address from given coordinate (longitude, latitude)
# 좌표(경도, 위도)로부터 주소를 조회합니다
@router.get("/get_address_by_coordinate")
async def read_address__by_coordinate(longitude: float, latitude: float):
    response = get_address_by_coordinate(longitude, latitude)
    return response

# Get real-time weather observation data based on coordinate
# 좌표에 기반한 초단기 실황(관측) 데이터를 조회합니다
@router.get("/get_ultra_srt_ncst_by_coordinate")
async def read_ultra_srt_ncst_by_coordinate(response: dict = Depends(get_ultra_srt_ncst_by_coordinate)):
    return response

# Get structured weather data list based on coordinate
# 좌표에 기반한 날씨 데이터 목록을 조회합니다
@router.get("/get_wthr_data_list_by_coordinate")
async def read_wthr_data_list_by_coordinate(response: dict = Depends(get_wthr_data_list_by_coordinate)):
    return response

# Get Naver search keywords based on trending queries
# 네이버 실시간 검색어 기반 키워드 목록을 조회합니다
@router.get("/get_naver_search_keywords")
async def read_naver_search_keywords(response: dict = Depends(get_naver_search_keywords)):
    return response

# Predict preferred cuisine types based on weather input
# 날씨 정보에 기반하여 추천 음식 종류를 예측합니다
@router.get("/predict_cuisine_type_by_weather")
async def read_predicted_cuisine_type_by_weather(response: dict = Depends(predict_cuisine_type_by_weather)):
    return response
