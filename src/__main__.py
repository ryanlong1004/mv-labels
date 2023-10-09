import os
from .discogs import get_data
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import json

directory = "C:\\Users\\ryanl\\Desktop\\I Want my MTV"


def process(path, artist, album, track, label):
    print(f"processing {path}")
    # clip = VideoFileClip(path).subclip(50, 55)
    clip = VideoFileClip(path).subclip(0, 5)
    w, h = clip.size

    print(TextClip.list("font"))
    exit()

    # Generate a text clip. You can customize the font, color, etc.
    txt_clip = TextClip(
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
        stroke_color="black",
        stroke_width=1,
        font="Kabel",
        method="caption",
        # size=(1080, 1920),
    ).set_position("left", "bottom")

    # Say that you want it to appear 10s at the center of the screen
    txt_clip = txt_clip.set_position(("left", "bottom")).set_duration(7)

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])

    # Write the result to a file (many options available !)
    video.write_videofile(f"{path.split('.')[0]}.mp4")


def main():
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            _path = f
            file_name = f.split("\\")[-1]
            try:
                artist, track = file_name.split(" - ")
                track = track.split("(")[0].split(".")[0]
                data = json.loads(get_data(artist, track))
                process(
                    _path,
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
