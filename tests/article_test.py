from fastapi.testclient import TestClient

from src.app import app

"""
PYTHONPATH=. pytest
"""

# Create a test client using the FastAPI app
# FastAPI 앱을 사용해 테스트 클라이언트를 생성
client = TestClient(app)

# Test reading a specific article by ID
# 특정 ID의 아티클을 조회하는 테스트
def test_read_article():
    response = client.get("/articles/10")
    # Check if the response status code is 200 (OK)
    # 응답 상태 코드가 200(정상)인지 확인
    assert response.status_code == 200

    # Check if the returned JSON matches the expected article data
    # 반환된 JSON이 기대한 아티클 데이터와 일치하는지 확인
    assert response.json() == {
        "title": "string",
        "preview_content": "string",
        "image": "string",
        "url": "string",
        "id": 10,
        "created_at": "2024-03-21T03:28:34.590682",
        "updated_at": "2024-03-21T03:28:34.590670"
    }

# Test reading a non-existent article
# 존재하지 않는 아티클을 조회하는 테스트
def test_read_nonexistent_article():
    response = client.get("/articles/9999")
    # Check if the response status code is 404 (Not Found)
    # 응답 상태 코드가 404(찾을 수 없음)인지 확인
    assert response.status_code == 404

    # Check if the returned JSON contains the expected error message
    # 반환된 JSON에 기대한 에러 메시지가 포함되어 있는지 확인
    assert response.json() == { "detail": "Not Found" }
