#!/usr/bin/env python3
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = config('CLIENTID')
client_secret = config('CLIENTSECRET')
username = config('USERNAME')
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# playlist_url = 'https://open.spotify.com/playlist/114JM3RIWLBz7f4j1dTYjU'

def is_valid(playlistURL):
	try:
		sp.user_playlist_tracks(username, playlist_url)
		return 'valid'
	except:
		return 'invalid'
		