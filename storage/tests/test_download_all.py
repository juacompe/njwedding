from django.test import TestCase
from storage.image_utils import download_all

class TestDownload(TestCase):
    def test_download_all_returns_list_of_image_paths(self):
        image_urls = ['http://p.twimg.com/AZh5jT2CEAAXyR-.jpg:large',
                      'http://distillery.s3.amazonaws.com/media/2011/09/17/bf5bb54387ca4dd98573128bb02f5c0b_7.jpg',
                      'http://s1-04.twitpicproxy.com/photos/large/425711171.jpg'] 
        image_paths = download_all(image_urls)
        expected = [u'httpp.twimg.comAZh5jT2CEAAXyR-.jpglarge',
                    u'httpdistillery.s3.amazonaws.commedia20110917bf5bb54387ca4dd98573128bb02f5c0b_7.jpg',
                    u'https1-04.twitpicproxy.comphotoslarge425711171.jpg']
        self.assertEqual(expected, image_paths)

