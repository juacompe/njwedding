from django.test import TestCase
from feed.fetch_twitter import parse_tweets, extract_urls_from_tweets
from feed.tests.twitter_test_content import raw_twitter_response
from json import loads

class TestParseTweets(TestCase): 
    def setUp(self):
        self.response_dict = loads(raw_twitter_response)

    def test_parsed_tweets_contains_twitpic(self):
        parsed_tweets = parse_tweets(self.response_dict)
        self.assertIn('test test test #njwedding http://t.co/cgGC89pO', parsed_tweets)

    def test_parsed_tweets_return_right_number_of_tweets(self):
        """
        There are 15 tweets in the raw_twitter_response
        """
        parsed_tweets = parse_tweets(self.response_dict)
        self.assertEqual(15, len(parsed_tweets))

    def test_extract_urls_from_tweets_excludes_None(self):
        """
        It should contain only url to download, None should be excluded
        """
        tweets = parse_tweets(self.response_dict)
        image_urls = extract_urls_from_tweets(tweets)
        self.assertNotIn(None, image_urls)
        