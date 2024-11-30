import googlemaps
from googlemaps import exceptions

gmaps = googlemaps.Client(key='AIzaSyCwmGf8z3FHyzy8itAOHK_4zj0kDY4JoI4')
_GEOLOCATION_BASE_URL = "https://www.googleapis.com"

result= gmaps.geolocate()
# 上記の取得情報一覧より緯度・経度の情報のみを抽出
lat = result["location"]["lat"]
lon = result["location"]["lng"]
print(lat,lon)