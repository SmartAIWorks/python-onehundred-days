from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json

def fetch_airasia_prices(origin="MNL", destination="MPH", date="2025-11-10"):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    #url = f"https://www.airasia.com/en/gb?origin={origin}&destination={destination}&departDate={date}&tripType=oneway"
    url = 'https://www.airasia.com/flights/search/?origin=MNL&destination=MPH&departDate=17%2F04%2F2026&tripType=R&returnDate=20%2F04%2F2026&adult=2&child=1&infant=0&locale=en-gb&currency=PHP&airlineProfile=all&type=paired&cabinClass=economy&upsellWidget=true&upsellPremiumFlatbedWidget=true&isOC=true&isDC=true&uce=true&ancillaryAbTest=false&providers=&taIDs='
    driver.get(url)

    time.sleep(10)  # wait for dynamic JS to load
    prices = []

    try:
        flight_cards = driver.find_elements(By.CSS_SELECTOR, ".Container__ContainerWrapper-sc-o4w52s-0")  # adjust selector
        print(flight_cards)
        for card in flight_cards:
            price_el = card.find_element(By.CSS_SELECTOR, ".Text__TextContainer-sc-xqubq8-0.gBxbny")
            flight_time = card.find_element(By.CSS_SELECTOR, ".flight-time").text
            prices.append({
                #"flight_time": flight_time,
                "price": price_el.text
            })
    except Exception as e:
        print("Error parsing flights:", e)

    driver.quit()
    return prices


if __name__ == "__main__":
    data = fetch_airasia_prices()
    print(json.dumps(data, indent=2))
