from decouple import config
import pandas as pd
import spotipy
from requests.exceptions import ReadTimeout
from spotipy.oauth2 import SpotifyClientCredentials
client_id = config('CLIENTID')
client_secret = config('CLIENTSECRET')
username = config('USERNAME')
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager,
                     requests_timeout=10, retries=10)

pd.options.mode.chained_assignment = None
def get_gen(filename):
    playlist = pd.read_csv('playlists/%s.csv' % filename)
    # df1 = pd.DataFrame(columns=['genre','popularity','result'])
    df1 = pd.DataFrame(columns=['genre', 'result'])
    playlist = playlist.join(df1, how="outer")

    for ind in playlist.index:
        playlist['result'][ind] = 1
        try:
            artist_data = sp.search(playlist['artist'][ind],
                                    limit=1, type="artist")
        except ReadTimeout:
            artist_data = sp.search(playlist['artist'][ind],
                                    limit=1, type="artist")
        try:
            artists_genre = artist_data["artists"]['items'][0]['genres']
        except IndexError:
            pass
        #SettingWithCopyWarning
        playlist['genre'][ind] = artists_genre
        print(ind)
    print('done')

    # for ind in playlist.index:
    #     try:
    #         song_data = sp.search(playlist['track'][ind],
    #                               limit=1, type="track")
    #     except ReadTimeout:
    #         song_data = sp.search(playlist['track'][ind],
    #                               limit=1, type="track")
    #     try:
    #         song_pop = song_data["tracks"]['items'][0]['popularity']
    #     except IndexError:
    #         pass
    #     df['popularity'][ind] = song_pop
    # print('done')

    playlist.to_csv('playlists/%s_ML.csv' % filename, encoding='utf-8', index=False)
