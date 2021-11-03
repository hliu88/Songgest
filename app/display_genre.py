import pandas as pd


def display_gen(filename) -> dict:
    playlist = pd.read_csv("playlists/%s_ML.csv" % filename)

    genre_cnt = {}
    for ind in playlist.index:
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
    return(genre_sorted)
