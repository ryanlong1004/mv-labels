"""Fetches informatino from discogs"""
import json
import logging
import discogs_client

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    handlers=[logging.FileHandler("archive_results.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

d = discogs_client.Client(
    "ExampleApplication/0.1", user_token="HHMdiPjbrzgqSIZqHlVbaVrmVUUhMvyUwApfzOUn"
)


def get_data(artist, track) -> str:
    """fetch artist - track data"""
    logger.debug("Fetching data")
    for x in d.search(f"{artist} -  {track}", type="title"):
        result = x.data
        result["album"] = x.main_release.title
        return json.dumps(result)
    return ""
