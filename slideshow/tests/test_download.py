from django.core.files.storage import default_storage
from django.test import TestCase
from slideshow.image_utils import download
from slideshow.image_utils import TWITTER_IMAGE_PATH

class TestDownload(TestCase):
    def setUp(self):
        image_name = 'https1.proxy03.twitpic.comphotoslarge399879761.jpg'
        self.image_path = TWITTER_IMAGE_PATH + image_name
        self.thumb_image_path = TWITTER_IMAGE_PATH + image_name

    def tearDown(self):
        default_storage.delete(self.image_path)
        default_storage.delete(self.thumb_image_path)
        
    # integration test
    def test_download(self):
        """
        Scenario: Download image, should download the image
        Expected:
        - image saved collected images and 
        - its thumbnail is generated
        """
        url = 'http://s1.proxy03.twitpic.com/photos/large/399879761.jpg'
        download(url)
        self.assertTrue(default_storage.exists(self.image_path))
        self.assertTrue(default_storage.exists(self.thumb_image_path))
