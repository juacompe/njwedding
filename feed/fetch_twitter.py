from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from feed.regex import get_image_url_from_raw_html
from httplib2 import Http 
from json import loads
from slideshow.image_utils import save_image

client = Http()

def fetch_twitter():
    response, content = fetch_tweets()
    if response.status == 200:
        write_to_file(content)
        image_urls = parse_tweets(loads(content))
        download_all(image_urls)
    
def download_all(image_urls):
    for image_url in image_urls:
        download(image_url)

def download(image_url):
    response, content = client.request(image_url)
    
    if response.status == 200 and response.get('content-type', None) == 'image/jpeg':
        image_name = default_storage.get_valid_name(image_url) 
        save_image(image_name, content)
    else:
        print '%s %s' % (response.status, response.get('content-type', None))

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

