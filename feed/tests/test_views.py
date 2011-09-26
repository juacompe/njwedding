from django.test import TestCase
from json import dumps

class TestViews(TestCase):
    def test_get_new_tweets_ok(self):
        response = self.client.get('/api/new_tweets/')
        self.assertEqual(200, response.status_code)

    def test_get_new_tweets_format(self):
        response = self.client.get('/api/new_tweets/')
        expected_response = {'max_id_str': '117972896940437504',
                             'next_page': '/api/new_tweets/after/117972896940437504',
                             'results': [
                                 {'id_str':'117972896940437504',
                                  'created_at': "Sun, 25 Sep 2011 14:45:05 +0000",
                                  'from_user': 'juacompe',
                                  'profile_image_url': 'http://a0.twimg.com/profile_images/1097051928/mypic2_normal.jpeg',
                                  'text': '@roofimon lets see if wp really anti-TDD',
                                 },
                                 {'id_str':'117540086551289857',
                                  'created_at': "Sat, 24 Sep 2011 10:05:15 +0000",
                                  'from_user': 'juacompe',
                                  'profile_image_url': 'http://a0.twimg.com/profile_images/1097051928/mypic2_normal.jpeg',
                                  'text': 'cleaned... http://t.co/48hQmTeM',
                                  'photo_url': 'http://localhost:8001/media/collected_twitter_images/httpmolo.mephotoswebbig0fkKTb'
                                 }
                             ]}
        self.assertEqual(dumps(expected_response), response.content)
