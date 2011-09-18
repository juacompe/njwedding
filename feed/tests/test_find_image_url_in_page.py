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

    def test_find_image_url_in_yfrog_page__found(self):
        page_url = 'http://yfrog.com/kg95174314j'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://desmond.yfrog.com/Himg736/scaled.php?tn=0&server=736&filename=95174314.jpg&xsize=640&ysize=640'
        self.assertEqual(expected_url, image_url)

    def test_find_image_url_in_molome_page__found(self):
        page_url = 'http://molo.me/p/2uvG77'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://molo.me/photos/webbig/2uvG77?key=28c68058869354c3cbdec54ecb15a0f6'
        self.assertEqual(expected_url, image_url)

#    def test_find_image_url_in_pic_twitter_page__found(self):
#        page_url = 'http://twitter.com/#!/igoyz/status/114975438018842624/photo/1'
#        image_url = find_image_url_in_page(page_url)
#        expected_url = 'http://p.twimg.com/AZh5jT2CEAAXyR-.jpg'
#        self.assertEqual(expected_url, image_url)

