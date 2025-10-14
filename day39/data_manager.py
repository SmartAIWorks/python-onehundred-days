
import os
from typing import Any, Dict, List, Optional

import requests

FLIGHT_DEALS_SHEET_URL = os.getenv('FLIGHT_DEALS_SHEET_URL', 'https://api.sheety.co/81c02c1cdaf065ccab8116f6cf1ee7b3/flightDeals/prices')

class DataManager:
    
    def __init__(self):
        self.session = requests.Session()

    def get_flight_deals(self) -> List[Dict[str, Any]]:
        ''' Return the flight deals from the google sheet'''
        response = self.session.get(url=FLIGHT_DEALS_SHEET_URL, timeout=10)
        response.raise_for_status()
        return response.json().get('prices', [])
    
    def update_flight_deals(self, data: Dict[str, Dict[str, str]] , id: str) -> None:
        ''' Update flight details'''
        put_url = f'{FLIGHT_DEALS_SHEET_URL}/{id}'
        response = self.session.put(url=put_url, json=data, timeout=10)
        response.raise_for_status()