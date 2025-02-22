import glob
import os

from constants import download_path, temp_reddit_folder


def clean_up_files():
    if not os.path.exists(download_path):
        raise "Download path doesn't exist"
    for file in glob.glob(download_path + '*'):
        print(f'Deleting file={file}...')
        os.remove(file)
    if os.path.isdir(os.path.join(download_path,temp_reddit_folder)):
        os.rmdir(temp_reddit_folder)
    