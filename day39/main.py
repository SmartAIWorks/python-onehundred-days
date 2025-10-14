from pprint import pprint
from typing import Any, Dict, List

from flight_search import FlightSearch
from data_manager import DataManager

from dotenv import load_dotenv

load_dotenv()

def main() -> None:
    data_manager = DataManager()
    flight_search = FlightSearch()
    sheet_data = data_manager.get_flight_deals()

    for s in sheet_data:
        if not s.get('iataCode'):
            iata = flight_search.get_destination_code(s.get('city', '')) or ""
            if not iata:
                continue

            new_data: Dict[str, Dict[str, str]] = {
                'price': {
                    'iataCode': iata
                }
            }

            data_manager.update_flight_deals(new_data, str(s.get('id', '')))


if __name__ == '__main__':
    main()