from django.core.files.storage import default_storage
from PIL import Image

TWITTER_IMAGE_PATH = 'collected_twitter_images/'
THUMBNAIL_PATH = TWITTER_IMAGE_PATH + 'thumbnails/' 
THUMBNAIL_SIZE = 60, 38

def collected_images():
    dir_names, file_names = default_storage.listdir(TWITTER_IMAGE_PATH)
    return file_names 

def create_thumbnail(image_name):
    image_path = default_storage.path(TWITTER_IMAGE_PATH + image_name)
    image = Image.open(image_path)
    image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
    thumbnail_path = default_storage.path(THUMBNAIL_PATH + image_name)
    image.save(thumbnail_path)
    return thumbnail_path

