import os
from dotenv import load_dotenv

# Load environment variables from .env file (with verbose output)
# .env 파일에서 환경 변수를 로드합니다 (verbose=True로 상세 출력)
load_dotenv(verbose=True)

# Secret key used to encode/decode JWT tokens (JWT 토큰 인코딩/디코딩에 사용되는 비밀 키)
AUTH_SECRET_KEY = os.getenv('AUTH_SECRET_KEY')

# Algorithm used for JWT encryption  (JWT 암호화에 사용되는 알고리즘)
AUTH_ALGORITHM = os.getenv('AUTH_ALGORITHM')

# Access token expiration time (in minutes) (액세스 토큰의 만료 시간 (단위: 분))
AUTH_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('AUTH_ACCESS_TOKEN_EXPIRE_MINUTES'))
