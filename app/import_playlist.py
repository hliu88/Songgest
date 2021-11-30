"""
import playlist from user provided url
"""
# 'https://open.spotify.com/playlist/114JM3RIWLBz7f4j1dTYjU'
# 'https://open.spotify.com/playlist/4VrP9ojSb5gm01kMru4jzj'
from decouple import config
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# import numexpr
# numexpr.set_num_threads(numexpr.detect_number_of_cores())
# ne.set_vml_num_threads(1)

client_id = config('CLIENTID')
client_secret = config('CLIENTSECRET')
username = config('USERNAME')
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def playlist_imp(playlist_url):
    """
    import playlist from url into CSV file
    """
    id_test = sp.user_playlist_tracks(username,
                                      playlist_url)['items'][0]['track']['id']
    columns = ['artist', 'track']
    list(map(lambda x: columns.append(x),
         list(sp.audio_features(id_test)[0].keys())))
    playlist_tracks = pd.DataFrame(columns=columns, index=range(0, 10000))
    playlist_total = sp.user_playlist_tracks(username,
                                             playlist_url, fields='total')
    number_of_songs = playlist_total["total"]
    row_counter = 0
    offset_val = 0
    playlist_total = sp.user_playlist_tracks(username,
                                             playlist_url, fields='total')
    number_of_songs = playlist_total["total"]
    max_val = number_of_songs

    while offset_val < max_val:
        for track in sp.user_playlist_tracks(username, playlist_url,
                                             offset=offset_val)['items']:
            current_id = track['track']['id']
            current_row = [track['track']['artists'][0]['name'],
                           track['track']['name']]
            (list(map(lambda x: current_row.append(x),
             list(sp.audio_features(current_id)[0].values()))))
            playlist_tracks.iloc[row_counter] = current_row
            row_counter += 1
        print(offset_val)
        offset_val += 100

    playlist_tracks.dropna(subset=['artist', 'track'])
    playlist_tracks.dropna(how="all", inplace=True)
    playlist_tracks.to_csv("playlists/%s.csv" % playlist_url[34:56],
                           encoding='utf-8', index=False)
    return number_of_songs

# def main():
#   playlist_imp()

# if __name__ == '__main__':
#   main()
