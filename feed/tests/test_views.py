from django.test import TestCase
from json import loads

class TestViews(TestCase):
    fixtures = ['two_tweets_fixture.json']
    #fixtures = ['tweets_from_db.json']

    def test_get_new_tweets_ok(self):
        response = self.client.get('/api/new_tweets/')
        self.assertEqual(200, response.status_code)

    def test_get_new_tweets_format(self):
        self.maxDiff = None
        response = self.client.get('/api/new_tweets/')
        expected_response = {u'max_id_str': u'117972896940437504',
                             u'next_page': u'/api/new_tweets/after/117972896940437504',
                             u'results': [
                                 {u'id_str':u'117972896940437504',
                                  u'created_at': u'2011-09-25 14:45:05',
                                  u'from_user': u'juacompe',
                                  u'profile_image_url': u'http://a0.twimg.com/profile_images/1097051928/mypic2_normal.jpeg',
                                  u'text': u'@roofimon lets see if wp really anti-TDD',
                                 },
                                 {u'id_str':u'117540086551289857',
                                  u'created_at': "Sat, 24 Sep 2011 10:05:15 +0000",
                                  u'from_user': u'juacompe',
                                  u'profile_image_url': u'http://a0.twimg.com/profile_images/1097051928/mypic2_normal.jpeg',
                                  u'text': u'cleaned... http://t.co/48hQmTeM',
                                  u'photo_url': u'http://localhost:8001/media/collected_twitter_images/httpmolo.mephotoswebbig0fkKTb'
                                 }
                             ]}
        self.assertDictEqual(expected_response, loads(response.content))
