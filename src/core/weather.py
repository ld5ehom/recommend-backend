import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

DATA_GO_KR_API_KEY_ENCODED = os.getenv('DATA_GO_KR_API_KEY_ENCODED')
DATA_GO_KR_API_KEY_DECODED = os.getenv('DATA_GO_KR_API_KEY_DECODED')
DATA_GO_KR_API_URL_USN = os.getenv('DATA_GO_KR_API_URL_USN')
DATA_GO_KR_API_URL_WDL = os.getenv('DATA_GO_KR_API_URL_WDL')
