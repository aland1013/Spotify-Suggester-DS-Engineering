
# viz.py

import flask_spotify
import math
from flask import jsonify

'''
Script to compile data from user input playlist and compare
similarites to suggested tracks.
'''

test = {
    "audio_features": [
        {
            "danceability": 0.808,
            "energy": 0.626,
            "key": 7,
            "loudness": -12.733,
            "mode": 1,
            "speechiness": 0.168,
            "acousticness": 0.00187,
            "instrumentalness": 0.159,
            "liveness": 0.376,
            "valence": 0.37,
            "tempo": 123.99,
            "type": "audio_features",
            "id": "4JpKVNYnVcJ8tuMKjAj50A",
            "uri": "spotify:track:4JpKVNYnVcJ8tuMKjAj50A",
            "track_href": "https://api.spotify.com/v1/tracks/4JpKVNYnVcJ8tuMKjAj50A",
            "analysis_url": "https://api.spotify.com/v1/audio-analysis/4JpKVNYnVcJ8tuMKjAj50A",
            "duration_ms": 535223,
            "time_signature": 4
        },
        {
            "danceability": 0.457,
            "energy": 0.815,
            "key": 1,
            "loudness": -7.199,
            "mode": 1,
            "speechiness": 0.034,
            "acousticness": 0.102,
            "instrumentalness": 0.0319,
            "liveness": 0.103,
            "valence": 0.389,
            "tempo": 96.083,
            "type": "audio_features",
            "id": "2NRANZE9UCmPAS5XVbXL40",
            "uri": "spotify:track:2NRANZE9UCmPAS5XVbXL40",
            "track_href": "https://api.spotify.com/v1/tracks/2NRANZE9UCmPAS5XVbXL40",
            "analysis_url": "https://api.spotify.com/v1/audio-analysis/2NRANZE9UCmPAS5XVbXL40",
            "duration_ms": 187800,
            "time_signature": 4
        },
        {
            "danceability": 0.281,
            "energy": 0.402,
            "key": 4,
            "loudness": -17.921,
            "mode": 1,
            "speechiness": 0.0291,
            "acousticness": 0.0734,
            "instrumentalness": 0.83,
            "liveness": 0.0593,
            "valence": 0.0793,
            "tempo": 115.7,
            "type": "audio_features",
            "id": "24JygzOLM0EmRQeGtFcIcG",
            "uri": "spotify:track:24JygzOLM0EmRQeGtFcIcG",
            "track_href": "https://api.spotify.com/v1/tracks/24JygzOLM0EmRQeGtFcIcG",
            "analysis_url": "https://api.spotify.com/v1/audio-analysis/24JygzOLM0EmRQeGtFcIcG",
            "duration_ms": 497493,
            "time_signature": 3
        }
    ]
}

# important features
important_features = ["danceability", "energy", "mode", "speechiness",
                      "instrumentalness", "liveness",
                      "valence"]

# round function
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

# function that returns averages of important features
def aggregate(df, key):
    key1 = key
    features = df.get("audio_features")
    keys = [feature[key1] for feature in features]
    average = abs(sum(keys)) / len(keys)
    return round_up(average, 4)
    # return keys


def viz_data(df):
    important_features = ["danceability", "energy", "mode", "speechiness",
                          "instrumentalness", "liveness",
                          "valence"]
    features = {}

    for i in important_features:
        features[i] = (aggregate(df, i))

    return features


def prediction(df):
    important_features = ["duration_ms", "key", "mode", "time_signature", "acousticness", "danceability",
                          "energy", "instrumentalness", "liveness", "loudness", "speechiness",
                          "valence", "tempo"]
    features = {}

    for i in important_features:
        features[i] = (aggregate(df, i))

    return features


if __name__ == "__main__":

    print(prediction(test))