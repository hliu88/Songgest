"""
checks valididty of the playlisturl
"""
# !/usr/bin/env python3
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = config('CLIENTID')
client_secret = config('CLIENTSECRET')
username = config('USERNAME')
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def is_valid(playlistURL):
    """
    checks valididty of url, returns bool
    """
    try:
        sp.user_playlist_tracks(username, playlistURL)
        return True
    except Exception:
        return False
