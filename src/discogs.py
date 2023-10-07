"""Fetches informatino from discogs"""


import discogs_client
import json

d = discogs_client.Client(
    "ExampleApplication/0.1", user_token="HHMdiPjbrzgqSIZqHlVbaVrmVUUhMvyUwApfzOUn"
)


def get_data(artist, track):
    """fetch artist - track data"""
    for x in d.search(f"{artist} -  {track}", type="title"):
        result = x.data
        result["album"] = x.main_release.title
        return json.dumps(x.data)
