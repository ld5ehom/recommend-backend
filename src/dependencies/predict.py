import numpy as np
import pandas as pd
import joblib

from src.core.ml import get_model_path, get_preprocessor_path
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

# Load the trained classification model using its path  
# 경로를 통해 학습된 분류 모델을 로드합니다
loaded_model = joblib.load(get_model_path())

# Load the preprocessing pipeline (e.g., StandardScaler)  
# 전처리 파이프라인을 로드합니다 (예: StandardScaler)
preprocessor = joblib.load(get_preprocessor_path())

# TODO : Update Naver Map API
def predict_cuisine_type_by_weather(temperature: float = 0.0, 
                                    precipitation: float = 0.0, 
                                    cloudiness: float = 0.0, 
                                    snowfall: float = 0.0, 
                                    pressure: float = 0.0,
                                    count: int = 2):
    
    # Create a DataFrame from the input weather features  
    # 입력된 날씨 데이터를 기반으로 DataFrame을 생성합니다
    new_weather_data = pd.DataFrame([[temperature, precipitation, cloudiness, snowfall, pressure]],
                                    columns=['Temperature', 'Precipitation', 'Cloudiness', 'Snowfall', 'Pressure'])

    # Apply preprocessing to scale the input features  
    # 입력 데이터를 전처리하여 스케일링합니다
    scaled_new_data = preprocessor.transform(new_weather_data)

    # Predict class probabilities for the input  
    # 입력에 대해 각 클래스의 확률을 예측합니다
    probs = loaded_model.predict_proba(scaled_new_data)

    # Select the top two most probable classes (highest probabilities)  
    # 확률이 가장 높은 상위 두 개의 클래스를 선택합니다
    best = np.argsort(probs, axis=1)[:,-2:]

    # Map indices to actual class labels in descending order of probability  
    # 확률이 높은 순서대로 클래스 레이블로 매핑합니다
    cuisine_types = [loaded_model.classes_[i] for i in best[0][::-1]]

    # Initialize the result dictionary  
    # 결과를 담을 딕셔너리를 초기화합니다
    result = {}
    rank = 1

    # Sort all classes by descending probability and store top N results  
    # 모든 클래스를 확률 기준으로 정렬하고 상위 N개만 결과에 저장합니다
    for p in np.argsort(-probs, axis=1)[0]: 
        result[loaded_model.classes_[p]] = {}
        result[loaded_model.classes_[p]]['rank'] = rank
        result[loaded_model.classes_[p]]['probability'] = probs[0][p]

        if rank >= count: break

        rank = rank + 1

    return result
