import os
from pathlib import Path
from .discogs import get_data
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    handlers=[logging.FileHandler("archive_results.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

directory = "./fixtures"


def get_text_clip(artist, track, album, label, w, h) -> TextClip:
    # Generate a text clip. You can customize the font, color, etc.
    return (
        TextClip(
            f"""
        {artist}
        \"{track}\"
        {album}
        {label}
        """,
            size=(w, h / 2),
            align="West",
            fontsize=h * 0.04,
            color="white",
            # stroke_color="black",
            # stroke_width=1,
            font="Kabel",
            method="caption",
            # size=(1080, 1920),
        )
        .set_position("left", "bottom")
        .set_duration(7)
    )


def process(_path: Path, artist, album, track, label):
    logging.debug(f"processing {_path.absolute()}")
    logging.debug(f"{artist} - {track}: {album}->{label}")
    path = str(_path.absolute())
    # clip = VideoFileClip(path).subclip(50, 55)
    clip = VideoFileClip(path).subclip(0, 5)
    w, h = clip.size

    # Generate a text clip. You can customize the font, color, etc.
    txt_clip = get_text_clip(artist, track, album, label, w, h)

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])

    # Write the result to a file (many options available !)
    video.write_videofile(f"{path.split('.')[0]}.mp4")


def get_artist_track(filename):
    """returns tuple of artist and track"""
    artist, track = filename.stem.split(" - ")
    track = track.split("(")[0]
    logging.debug(f"Found {artist}, {track}")
    return (artist, track)


def main():
    for filename in [Path.joinpath(Path(directory), x) for x in os.listdir(directory)]:
        # checking if it is a file
        artist, track = get_artist_track(filename)

        try:
            data = json.loads(get_data(artist, track))
            process(
                filename,
                artist,
                data["album"],
                track,
                data["label"][0],
            )
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    main()
