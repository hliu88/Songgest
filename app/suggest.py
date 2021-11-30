from decouple import config
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_id = config('CLIENTID')
client_secret = config('CLIENTSECRET')
username = config('USERNAME')


client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager,
                     requests_timeout=10, retries=10)


column_drop = ['artist', 'track', 'type', 'id', 'uri', 'track_href',
               'analysis_url', 'duration_ms', 'time_signature',
               'genre']
genre_column_drop = ['artist', 'track', 'danceability', 'energy', 'key',
                     'loudness', 'mode', 'speechiness', 'acousticness',
                     'instrumentalness', 'liveness', 'valence', 'tempo',
                     'type', 'id', 'uri', 'track_href',
                     'analysis_url', 'duration_ms', 'time_signature']
column_rec_drop = ['artist', 'track', 'type', 'id', 'uri', 'track_href',
                   'analysis_url', 'duration_ms', 'time_signature']


def train_model(x_train, y_train):
    """
    trains neural network
    """
    model = Sequential()
    model.add(Dense(11, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(33, activation='relu'))
    model.add(Dense(33, activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam',
                  metrics=['accuracy'])
    # model.fit(x_train, y_train, epochs=150, batch_size=10)
    model.fit(x_train, y_train, epochs=50, batch_size=10)
    # yhat = (model.predict(x_test) > 0.5).astype(int)
    return model


def ML(filename):
    """
    Classify songs with training model, then suggests songs and
    compare against traning model
    """
    playlist = pd.read_csv('playlists/master_ML.csv')
    master = pd.read_csv('playlists/%s_ML.csv' % filename)
    playlist2 = playlist.drop(columns=column_drop+['popularity'])
    playlist3 = master.drop(columns=column_drop)
    frames = [playlist2, playlist3]
    result = pd.concat(frames)
    for i in range(20):
        frames1 = [playlist3, result]
        result = pd.concat(frames1)
    p = result.values
    x = p[:, :11]
    y = p[:, -1]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15)

    model = train_model(x_train, y_train)

    # yhat = (model.predict(x_test) > 0.5).astype(int)
    # function
    genre_cnt = {}
    for ind in master.index:
        a = playlist['genre'][ind]
        a = a.replace("'", '')
        a = a.replace("'", "")
        a = a.strip('[]')
        b = a.split(',')
        for i in range(len(b)):
            b[i] = b[i].strip()
        for genre in b:
            if genre in genre_cnt:
                genre_cnt[genre] += 1
            else:
                genre_cnt[genre] = 1
    genre_sorted = sorted(genre_cnt.items(), key=lambda x: x[1], reverse=True)

    rec_playlist = []
    for i in range(10):
        try:
            genre_x = [genre_sorted[i][0]]
            track = sp.recommendations(seed_genres=genre_x, limit=100)
            for x in track['tracks']:
                id = x['id']
                name = x['artists'][0]['name']
                tra = x['name']
                rec_playlist.append([tra, name, id])
        except Exception:
            pass

    rec_tracks = pd.DataFrame(columns=genre_column_drop,
                              index=range(0, len(rec_playlist)))
    for i in range(len(rec_playlist)):
        current_row = [rec_playlist[i][0], rec_playlist[i][1]]
        trackz = [rec_playlist[i][2]]
        (list(map(lambda x: current_row.append(x), list(sp.audio_features
              (tracks=trackz)[0].values()))))
        rec_tracks.iloc[i] = current_row

    rec_tracks_dropped = rec_tracks.drop(columns=column_rec_drop)
    rec_tracks_dropped_y = rec_tracks_dropped.iloc[:, :11]
    rec_tracks_dropped_y.values
    rec_tracks_dropped_y = np.asarray(rec_tracks_dropped_y).astype(np.float32)
    yhat_pred = (model.predict(rec_tracks_dropped_y) > 0.5).astype(int)

    df = pd.DataFrame(columns=['result'])
    rec_tracks = rec_tracks.join(df, how="outer")
    rec_tracks = rec_tracks.sort_index()
    for ind in rec_tracks.index:
        rec_tracks['result'][ind] = yhat_pred[ind][0]
    rec_tracks = rec_tracks[rec_tracks.result != 0]

    # sp.user_playlist_create(username, filename,
    #                         public=True, description='test')
    # track_list = list(rec_tracks['id'])
    # sp.user_playlist_add_tracks(username,
    #                             playlist_id=filename, tracks=track_list)
    # return(rec_tracks.shape[0])
    if(rec_tracks.shape[0] == 0):
        return(["Inconclusive Result"])
    return(rec_tracks['artist'].values.tolist())
