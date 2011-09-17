from django.conf import settings
from django.core.files.storage import default_storage
from django.test import TestCase
from slideshow.image_utils import create_thumbnail

class TestCreateThumbnail(TestCase):
    def test_thumbnail_exists_after_created(self):
        image_name = '132883093_49660b8f2a_z.jpg'
        
        path = create_thumbnail(image_name) 

        self.assertTrue(default_storage.exists(path))

    def test_thumbnail_created_at_right_path(self):
        image_name = '132883093_49660b8f2a_z.jpg'

        created_path = create_thumbnail(image_name) 

        thumbnail_path = 'collected_twitter_images/thumbnails/' + image_name
        expected_path = default_storage.path(thumbnail_path)
        self.assertEqual(created_path, expected_path)

        
