import requests

from os import path
from moviepy import VideoFileClip
from instaloader import Post, Instaloader
from constants import download_path, default_video_name, default_audio_name


def download_reel_video(reel_id):
        L = Instaloader()
        post = Post.from_shortcode(L.context, str(reel_id))
        url = post.video_url
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(path.join(download_path, default_video_name), 'wb') as video:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        video.write(chunk)


def get_audio_from_video():
    video = VideoFileClip(path.join(download_path, default_video_name))
    video.audio.write_audiofile(path.join(download_path, default_audio_name))