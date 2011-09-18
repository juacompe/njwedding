from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from httplib2 import Http
from PIL import Image
from StringIO import StringIO

TWITTER_IMAGE_PATH = 'collected_twitter_images/'
THUMBNAIL_PATH = TWITTER_IMAGE_PATH + 'thumbnails/' 
THUMBNAIL_SIZE = 60, 38

client = Http()

def collected_images():
    dir_names, file_names = default_storage.listdir(TWITTER_IMAGE_PATH)
    return file_names 

def create_thumbnail(image_name):
    image_path = default_storage.path(TWITTER_IMAGE_PATH + image_name)
    image = Image.open(image_path)
    image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
    thumbnail_path = default_storage.path(THUMBNAIL_PATH + image_name)
    if (image_path.lower()).find('jpg') <= -1:
        thumbnail_path=thumbnail_path+'.jpg'
    image.save(thumbnail_path)
    return thumbnail_path

def save_image(image_name, content):
    verifying_image = Image.open(ContentFile(StringIO(content).buf))
    verifying_image.verify()
    # verify occationally cause image.fp to be None -*-
    image = Image.open(ContentFile(StringIO(content).buf))
    image_path = default_storage.path(TWITTER_IMAGE_PATH + image_name)
    #if (image_path.lower()).find('jpg') <= -1:
    #    image_path=image_path+'.jpg'
    image.save(image_path,'JPEG')
    #image.save(image_path)
    create_thumbnail(image_name)

def download_all(image_urls):
    for image_url in image_urls:
        download(image_url)

def download(image_url):
    response, content = client.request(image_url)
    
    #if response.status == 200 and response.get('content-type', None) == 'image/jpeg':
    if response.status == 200:
        image_url = image_url.split('?')[0] # chop the query string out
        image_name = default_storage.get_valid_name(image_url) 
        save_image(image_name, content)
    else:
        log.error('%s %s' % (response.status, response.get('content-type', None)))

