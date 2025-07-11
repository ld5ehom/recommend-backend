from fastapi.testclient import TestClient

from src.app import app

"""
PYTHONPATH=. pytest
"""

# Create a test client instance using the FastAPI app
# FastAPI 앱을 이용하여 테스트 클라이언트를 생성합니다
client = TestClient(app)

# Test the ML prediction API under the utilities route
# utilities 라우터에서 머신러닝 예측 API를 테스트합니다
def test_read_ml_on_utilities():
    params = {
        'temperature': 0.0, 
        'precipitation': 0.0, 
        'cloudiness': 0.0, 
        'snowfall': 0.0, 
        'pressure': 0.0,
        'count': 2
    }

    # Send GET request to predict cuisine types based on weather
    # 날씨 데이터를 기반으로 요리 유형을 예측하는 GET 요청을 보냅니다
    response = client.get("/utilities/predict_cuisine_type_by_weather", params=params)
    
    # Ensure the response is successful (HTTP 200)
    # 응답이 성공적으로 반환되었는지 확인합니다 (HTTP 200)
    assert response.status_code == 200

# Test the restaurant endpoint that includes ML weather prediction
# 날씨 기반 머신러닝 예측이 포함된 레스토랑 API를 테스트합니다
def test_ml_in_restaurants():
    params = {
        'longitude': 127.032261050, 
        'latitude': 37.498408928, 
        'distance': 2,
    }

    # Send GET request to fetch restaurants with filtering by coordinates
    # 좌표 기반 필터링으로 레스토랑을 조회하는 GET 요청을 보냅니다
    response = client.get("/restaurants", params=params)
    
    # Ensure the response is successful (HTTP 200)
    # 응답이 성공적으로 반환되었는지 확인합니다 (HTTP 200)
    assert response.status_code == 200
