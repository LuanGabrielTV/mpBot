from os import path
from moviepy import VideoFileClip
from constants import download_path, default_video_name, default_audio_name
from urllib.parse import urlparse
from strategy import social_networks

def download_video(url):
    parsed_url = urlparse(url)
    print(parsed_url.netloc)
    try:
        social_networks[parsed_url.netloc](url)
    except:
        raise Exception('O site não pode ser acessado')

def get_audio_from_video():
    video = VideoFileClip(path.join(download_path, default_video_name))
    video.audio.write_audiofile(path.join(download_path, default_audio_name))
