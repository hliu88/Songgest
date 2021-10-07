#!/usr/bin/env python3
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = config('CLIENTID')
client_secret = config('CLIENTSECRET')
username = config('USERNAME')
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def is_valid(playlistURL):
    try:
        sp.user_playlist_tracks(username, playlistURL)
        return 'valid'
    except Exception:
        return 'invalid'

# def main():
# 	is_valid('https://open.spotify.com/playlist/114JM3RIWLBz7f4j1dTYjU?si=a084fb36f5004f6e')

# if __name__ == '__main__':
# 	main()
