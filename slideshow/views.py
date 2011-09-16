from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    context = RequestContext(request)
    context['IMAGE_URL'] = settings.MEDIA_URL + 'collected_twitter_images/'
    context['THUMBNAIL_URL'] = settings.MEDIA_URL + 'collected_twitter_images/thumbnails/'
    return render_to_response('home.html', context_instance=context)
