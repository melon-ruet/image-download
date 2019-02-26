import os

download_dir = 'images'


def download_images(image_file):
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
