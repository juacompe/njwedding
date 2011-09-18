from django.test import TestCase
from feed.fetch_twitter import find_image_url_in_page

class TestFindImageUrlInPage(TestCase):
    def test_find_image_url_in_twitpic_page__found(self):
        page_url = 'http://twitpic.com/6m2t75'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://s1.proxy03.twitpic.com/photos/large/399879761.jpg'
        self.assertEqual(expected_url, image_url)

    def test_find_image_url_in_lockerz_page__found(self):
        page_url = 'http://lockerz.com/s/139778407'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://c0013959.cdn1.cloudfiles.rackspacecloud.com/x2_854d967'
        self.assertEqual(expected_url, image_url)

