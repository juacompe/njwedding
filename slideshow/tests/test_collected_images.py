from django.test import TestCase
from slideshow.image_utils import collected_images, TWITTER_IMAGE_PATH
from django.core.files.storage import default_storage

class TestCollectedImages(TestCase):
    def setUp(self):
        # generate sample image
        image_name = '132883093_49660b8f2a_z.jpg'
        image_path = TWITTER_IMAGE_PATH + image_name
        image = default_storage.open(image_path)
        # saving same name will created a new file_1
        self.test_image_name = 'test_collected_images__' + image_name
        test_image_path = TWITTER_IMAGE_PATH + self.test_image_name
        self.test_image_path = default_storage.save(test_image_path, image)

    def tearDown(self):
        # delete sample image
        default_storage.delete(self.test_image_path)
        
    def test_collected_images(self):
        images = collected_images() 
        self.assertIn(self.test_image_name, images)

