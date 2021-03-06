import os
import shutil
from unittest import TestCase

from download import download_images, download_dir


class DownloadTest(TestCase):

    def test_download_files(self):
        test_image_file = 'images.txt'
        self.assertEqual(os.path.exists(test_image_file), True, 'Test image file not found')
        download_images(test_image_file)
        self.assertEqual(os.path.exists(download_dir), True, 'Download dir not found')
        with open(test_image_file) as file:
            count = len(file.readlines())
        self.assertEqual(len(os.listdir(download_dir)), count, 'All files download failed')
        shutil.rmtree(download_dir)
