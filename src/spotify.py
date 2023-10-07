import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import os

os.environ["SPOTIPY_CLIENT_ID"] = "XXXXXXXXXXXXXXXXXXXXXXXXX"
os.environ["SPOTIPY_CLIENT_SECRET"] = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.search(q="artist: Counting Crows", type="artist")
artist_iri = "https://open.spotify.com/artist/0vEsuISMWAKNctLlUAhSZC"

albums = results["items"]
while results["next"]:
    results = spotify.next(results)
    albums.extend(results["items"])

for album in albums:
    print(album["name"])
