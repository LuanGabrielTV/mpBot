import os
import shutil

from constants import download_path

def clean_up_files():
    if not os.path.exists(download_path):
        raise "Download path doesn't exist"
    shutil.rmtree(download_path)
    os.mkdir(download_path)
    