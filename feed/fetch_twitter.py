from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from feed.regex import get_image_url_from_raw_html
from httplib import BadStatusLine
from httplib2 import Http, ServerNotFoundError
from json import loads
from storage.image_utils import download_all 
import logging

client = Http()
log = logging.getLogger(__name__)

def fetch_twitter():
    response, content = fetch_tweets()
    if response.status == 200:
        write_to_file(content)
        tweets = parse_tweets(loads(content))
        image_urls = extract_urls_from_tweets(tweets)
        download_all(image_urls)
    
def fetch_tweets():
    """
    Fetch tweets according to TWITTER_QUERY in django's settings and return
    response and python dict of the returned tweets.
    """
    query = settings.TWITTER_QUERY
    twitter_search_url = 'http://search.twitter.com/search.json?q=%s' % query
    response, content = client.request(twitter_search_url) 
    return response, content

def write_to_file(content):
    """
    Write `content` into /media/search.json
    """
    #read existing content
    exiting_content = default_storage.open('search.json').read()
    #save existing content to backup
    path = default_storage.save('search.json', ContentFile(exiting_content))
    #delete current search.json
    default_storage.delete('search.json')
    #save new content to search.json, so search.json has the latest content from twitters
    path = default_storage.save('search.json', ContentFile(content))

def parse_tweets(result_dict):
    results = result_dict['results']
    return [ tweet['text'] for tweet in results ]

def extract_urls_from_tweets(tweets):
    image_urls = []
    for tweet in iter(tweets):
        urls = find_url_in_tweet(tweet)
        for url in iter(urls):
            try:
                image_url = find_image_url_in_page(url)
            except ServerNotFoundError, e:
                log.error('fail to find photo in url %s' % url)
                log.exception(e)
            except BadStatusLine, e:
                log.error('fail to find photo in url %s' % url)
                log.exception(e)
                
            if image_url is not None:
                image_urls.append(image_url)
    return image_urls

def find_image_url_in_page(url):
    """
    Open the page, find the photo in the page, and return url of the photo 
    image.
    """
    response, content = client.request(url)
    image_url = None
    if is_twitpic_response(response):
        regex_text='id="photo-display" src="(?P<src>.+?)"'
        image_url = get_image_url_from_raw_html(content, regex_text)
    return image_url
    
def is_twitpic_response(response):
    location = response.get('content-location', '')
    return location.find('http://twitpic.com') > -1
    
def find_url_in_tweet(text):
    words = text.split(' ')
    urls = [ word for word in words if word.count('http://') ]
    return urls 

