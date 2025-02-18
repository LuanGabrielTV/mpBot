import requests

from constants import download_path, default_video_name 
from redvid import Downloader

def download_reddit_video(url):
    reddit = Downloader(max_q=True)
    reddit.overwrite = True
    reddit.url = url
    reddit.filename = default_video_name
    reddit.path = download_path
    reddit.download()    