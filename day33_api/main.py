import requests

from requests import Response


response: Response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

content = response.json()

long = content.get('iss_position', {}).get('longitude', '')
lat = content.get('iss_position', {}).get('latitude', '')

long_lat = (long, lat)

print(long_lat)
