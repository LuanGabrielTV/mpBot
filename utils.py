import glob

from os import path, remove
from constants import download_path

def clean_up_files():
    if not path.exists(download_path):
        raise "Download path doesn't exist"
    for file in glob.glob(download_path + '*'):
        print(f'Deleting file={file}...')
        remove(file)
    