import requests, datetime, logging
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from spotify_manager import SpotifyManager
load_dotenv()


def get_user_input() -> str:
    while True:
        date_str = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except Exception:
            print('Invalid date. Please use YYYY-MM-DD.')


BILL_BOARD_URL = 'https://www.billboard.com/charts/hot-100/'


def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    user_input = get_user_input()
    top_url = BILL_BOARD_URL + user_input

    logging.info(f'Fetching Billboard Hot 100 for {user_input} ...')
    response = requests.get(top_url, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    song_names_spans = soup.select('li ul li h3')
    if not song_names_spans:
        raise RuntimeError('No songs found on the page. The Billboard markup may have changed.')

    song_names = [song.get_text().strip() for song in song_names_spans]
    logging.info(f'Scraped {len(song_names)} songs.')

    spotify = SpotifyManager()
    current_user = spotify.sp.current_user()
    user_id = current_user['id'] if current_user else ''

    if not user_id:
        raise ValueError('Invalid Spotify user. Check authentication/environment variables.')

    track_year = datetime.datetime.strptime(user_input, '%Y-%m-%d')
    track_uris = spotify.build_song_track(song_names, track_year.year)
    logging.info(f'Resolved {len(track_uris)} tracks on Spotify.')

    logging.info('Creating playlist...')
    play_list_id = spotify.create_playlist(user_id=user_id, name=f'{user_input} Billboard 100')

    logging.info('Adding items to playlist...')
    spotify.add_items_to_playlist(playlist_id=play_list_id, song_uris=track_uris)

    logging.info('Completed successfully!')


    


    

if __name__ == '__main__':
    main()