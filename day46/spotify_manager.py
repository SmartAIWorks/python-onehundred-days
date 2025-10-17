
from dotenv import load_dotenv

import spotipy, os, time
from typing import List
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()


class SpotifyManager:
    def __init__(self) -> None:
        client_id = os.getenv('SPOTIFY_CLIENT_ID')
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI', 'https://example.com')
        scope = os.getenv('SPOTIFY_SCOPE', 'playlist-modify-private')

        if not client_id or not client_secret:
            raise EnvironmentError('Missing SPOTIFY_CLIENT_ID or SPOTIFY_CLIENT_SECRET in environment')

        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope=scope,
                redirect_uri=redirect_uri,
                client_id=client_id,
                client_secret=client_secret
            )
        )

    def build_song_track(self, songs: List[str], year: int) -> List[str]:
        uris: List[str] = []
        for song in songs:
            query = f'track:{song} year:{year}'
            try:
                result = self.sp.search(q=query, type='track', limit=1)
                items = result.get('tracks', {}).get('items', []) if result else []
                if items:
                    uris.append(items[0]['uri'])
                else:
                    # Fallback: try without year constraint
                    fallback = self.sp.search(q=f'track:{song}', type='track', limit=1)
                    fallback_items = fallback.get('tracks', {}).get('items', []) if fallback else []
                    if fallback_items:
                        uris.append(fallback_items[0]['uri'])
                    else:
                        print(f"No Spotify match found for: {song}")
                time.sleep(0.05)  # be gentle with rate limits
            except spotipy.SpotifyException as e:
                print(f"Spotify error for '{song}': {e}")
            except Exception as e:
                print(f"Unexpected error for '{song}': {e}")

        return uris

    def create_playlist(self, user_id: str, name: str) -> str:
        result = self.sp.user_playlist_create(user=user_id, name=name, public=False)
        if result and 'id' in result:
            return result['id']
        raise RuntimeError('Failed to create playlist')

    def add_items_to_playlist(self, playlist_id: str, song_uris: List[str]) -> None:
        # Spotify API allows up to 100 items per request
        chunk_size = 100
        for i in range(0, len(song_uris), chunk_size):
            chunk = song_uris[i:i + chunk_size]
            self.sp.playlist_add_items(playlist_id=playlist_id, items=chunk)
