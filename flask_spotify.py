from flask import Flask, jsonify, request, render_template
import pickle
import json

app = Flask(__name__)

JSON =  {
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

@app.route("/")
def main():
  return render_template("main.html")

@app.route("/return", methods=['POST'])
def JSON_Object():
    return jsonify({
        "object": dict(request.form)
    })


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)