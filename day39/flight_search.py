import os
from typing import Optional
import requests

class FlightSearch:

    AMADEUS_TOKEN_URL = 'https://test.api.amadeus.com/v1/security/oauth2/token'
    AMADEUS_BASE_URL = 'https://test.api.amadeus.com/v1'
    AMADEUS_CITIES_URL = f'{AMADEUS_BASE_URL}/reference-data/locations/cities'

    def __init__(self):
        self.session = requests.Session()
        self.app_id = os.getenv('AMADEUS_APP_ID')
        self.api_key = os.getenv('AMADEUS_API_KEY')
        self.token: Optional[str] = None
        self.generate_token()

    def get_destination_code(self, city: str) -> Optional[str]:
        return self.get_cities(city)

    def get_cities(self, keyword: str) -> Optional[str]:
        if not keyword:
            return None

        headers = {
            'Authorization': f'Bearer {self.token}',
            'Accept': 'application/json'
        }

        params = {
            'keyword': keyword,
            'max': '2',
            'include': 'AIRPORTS',
        }

        response = self.session.get(url=self.AMADEUS_CITIES_URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json().get('data', [])
        if not data:
            return None

        first = data[0] or {}
        return first.get('iataCode') or None

    def generate_token(self) -> None:
        if not self.app_id or not self.api_key:
            raise RuntimeError('AMADEUS_APP_ID and AMADEUS_API_KEY must be set in environment variables')

        data = {
            'grant_type': 'client_credentials',
            'client_id': self.app_id,
            'client_secret': self.api_key
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = self.session.post(url=self.AMADEUS_TOKEN_URL, data=data, headers=headers, timeout=10)
        response.raise_for_status()
        self.token = response.json().get('access_token')
        if not self.token:
            raise RuntimeError('Failed to obtain Amadeus access token')