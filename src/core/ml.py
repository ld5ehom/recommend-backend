import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

ML_MODEL_DIR = os.getenv('ML_MODEL_DIR')
ML_MODEL_VERSION = os.getenv('ML_MODEL_VERSION')
ML_MODEL_FILE = os.getenv('ML_MODEL_FILE')
ML_PREPROCESSOR_FILE = os.getenv('ML_PREPROCESSOR_FILE')

def get_model_path():
  return os.path.join(ML_MODEL_DIR, ML_MODEL_VERSION, ML_MODEL_FILE)

def get_preprocessor_path():
  return os.path.join(ML_MODEL_DIR, ML_MODEL_VERSION, ML_PREPROCESSOR_FILE)
