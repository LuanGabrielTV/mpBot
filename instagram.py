import requests

from instaloader import Post, Instaloader
from http import HTTPStatus
from utils import clean_up_files
from os import path
from constants import download_path, default_video_name, separator


def download_reel_video(url):
    reel_id = url[31:].split(separator, 1)[0]
    clean_up_files()
    instaloader = Instaloader()
    post = Post.from_shortcode(instaloader.context, str(reel_id))
    url = post.video_url
    response = requests.get(url, stream=True)
    if response.status_code == HTTPStatus.OK:
        with open(path.join(download_path, default_video_name), 'wb') as video:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    video.write(chunk)