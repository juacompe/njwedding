from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from feed.regex import get_image_url_from_raw_html
from httplib2 import Http 
from json import loads

client = Http()

def fetch_twitter():
    response, content = fetch_tweets()
    if response.status == 200:
        write_to_file(content)
        parse_tweets(loads(content))
    
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
    path = default_storage.save('search.json', ContentFile(content))

def parse_tweets(result_dict):
    results = result_dict['results']
    for tweet in results:
        text = tweet['text']
        urls = find_url_in_tweet(text)
        image_urls = [ find_image_url_in_page(url) for url in urls ]
    return image_urls

def find_image_url_in_page(url):
    """
    Open the page, find the photo in the page, and return url of the photo 
    image.
    """
    response, content = client.request(url)
    image_url = None
    if is_twitpic_response(response):
        image_url = get_image_url_from_raw_html(content)
    return image_url
    
def is_twitpic_response(response):
    location = response.get('content-location', '')
    return location.find('http://twitpic.com') > -1
    
def find_url_in_tweet(text):
    words = text.split(' ')
    urls = [ word for word in words if word.count('http://') ]
    return urls 
