from django.core.files.storage import default_storage
from PIL import Image

TWITTER_IMAGE_PATH = 'collected_twitter_images/'
THUMBNAIL_PATH = TWITTER_IMAGE_PATH + 'thumbnails/' 
THUMBNAIL_SIZE = 60, 38

def collected_images():
    images = ['132883093_49660b8f2a_z.jpg',
              '399107666.jpg',
              '2957442267_6afce8dd8f_z.jpg',
              '5975249429_4c076b25c1_z.jpg',
              '6041022237_287ede031f_z.jpg',]
    return images

def create_thumbnail(image_name):
    image_path = default_storage.path(TWITTER_IMAGE_PATH + image_name)
    image = Image.open(image_path)
    image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
    thumbnail_path = default_storage.path(THUMBNAIL_PATH + image_name)
    image.save(thumbnail_path)
    return thumbnail_path

