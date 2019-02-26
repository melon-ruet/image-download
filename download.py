import os
import sys
import urllib.request

download_dir = 'images'


def download_images(image_file):
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

    with open(image_file, 'r') as file:
        for line in file:
            urllib.request.urlretrieve(line, download_dir + os.sep + line.split('/')[-1] + '.jpg')


if __name__ == '__main__':
    download_images(sys.argv[-1])
