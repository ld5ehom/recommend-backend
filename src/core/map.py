import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

VWORLD_API_URL = os.getenv('VWORLD_API_URL')
VWORLD_API_KEY = os.getenv('VWORLD_API_KEY')
