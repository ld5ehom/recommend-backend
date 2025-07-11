import requests

def get_naver_search_keywords(query: str, format: str = "json"):
    url = "https://mac.search.naver.com/mobile/ac"
    params ={
        "q": query,
        "con": 0,
        "q_enc":"UTF-8",
        "st":1,
        "frm": "mobile_nv",
        "r_format": format,
        "r_enc":"UTF-8",
        "r_unicode":0,
        "t_koreng":1,
        "ans":2,
        "run":2,
        "rev":4
    }

    response = requests.get(url, params=params)
    
    return response.json()
