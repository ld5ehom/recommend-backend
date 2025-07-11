import requests
import math

from src.core.map import VWORLD_API_URL, VWORLD_API_KEY

# Get coordinate (longitude, latitude) from road name address using VWorld API
# 도로명 주소를 위경도 좌표로 변환합니다 (VWorld API 사용)
def get_coordinate_by_address(address: str, format: str = "json"):
    params = {
        "service": "address",
        "request": "getcoord",
        "crs": "epsg:4326",
        "address": address,
        "format": format,
        "type": "road",
        "key": VWORLD_API_KEY
    }

    response = requests.get(VWORLD_API_URL, params=params)
    return response.json()

# Get road name address from coordinate (longitude, latitude) using VWorld API
# 위경도 좌표로 도로명 주소를 조회합니다 (VWorld API 사용)
def get_address_by_coordinate(longitude: float, latitude: float, format: str = "json"):
    params = {
        "service": "address",
        "request": "getaddress",
        "crs": "epsg:4326",
        "point": "%s,%s" % (longitude, latitude),
        "format": format,
        "type": "road",
        "key": VWORLD_API_KEY
    }

    response = requests.get(VWORLD_API_URL, params=params)
    return response.json()


# Constants for latitude/longitude to grid coordinate conversion
# 위경도를 격자 좌표로 변환하기 위한 상수 정의
NX = 149
NY = 253
Re = 6371.00877
grid = 5.0
slat1 = 30.0
slat2 = 60.0
olon = 126.0
olat = 38.0
xo = 210 / grid
yo = 675 / grid
first = 0

# Initialize projection constants
# 격자 변환을 위한 투영 상수들을 초기화합니다
if first == 0:
    PI = math.asin(1.0) * 2.0
    DEGRAD = PI / 180.0
    RADDEG = 180.0 / PI

    re = Re / grid
    slat1 = slat1 * DEGRAD
    slat2 = slat2 * DEGRAD
    olon = olon * DEGRAD
    olat = olat * DEGRAD

    sn = math.tan(PI * 0.25 + slat2 * 0.5) / math.tan(PI * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(PI * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(PI * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn)
    first = 1

# Convert latitude and longitude to grid coordinate (x, y)
# 위도, 경도를 격자 좌표 x, y로 변환합니다
def get_grid_by_coordinate(lat: float, lon: float, code=0):
    ra = math.tan(PI * 0.25 + lat * DEGRAD * 0.5)
    ra = re * sf / pow(ra, sn)
    theta = lon * DEGRAD - olon
    if theta > PI:
        theta -= 2.0 * PI
    if theta < -PI:
        theta += 2.0 * PI
    theta *= sn
    x = (ra * math.sin(theta)) + xo
    y = (ro - ra * math.cos(theta)) + yo
    x = int(x + 1.5)
    y = int(y + 1.5)
    return x, y

# Convert grid coordinate (x, y) back to latitude and longitude
# 격자 좌표 x, y를 위도, 경도로 변환합니다
def get_coordinate_by_grid(x: float, y: float, code=1):
    x = x - 1
    y = y - 1
    xn = x - xo
    yn = ro - y + yo
    ra = math.sqrt(xn * xn + yn * yn)
    if sn < 0.0:
        ra = -ra
    alat = math.pow((re * sf / ra), (1.0 / sn))
    alat = 2.0 * math.atan(alat) - PI * 0.5
    if math.fabs(xn) <= 0.0:
        theta = 0.0
    else:
        if math.fabs(yn) <= 0.0:
            theta = PI * 0.5
            if xn < 0.0:
                theta = -theta
        else:
            theta = math.atan2(xn, yn)
    alon = theta / sn + olon
    lat = alat * RADDEG
    lon = alon * RADDEG
    return lat, lon
