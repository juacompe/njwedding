from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'slideshow.views.home', name='home'),
    url(r'^api/new_tweets/$', 'feed.views.new_tweets', name='new_tweets'),
    (r'^about/$',direct_to_template, {'template': 'about.html'}),
    (r'^guestbook/$',direct_to_template, {'template': 'guestbook.html'}),
    (r'^gallery/$',direct_to_template, {'template': 'nj_gallery.html'}),
    url(r'^testjs/', include('testjs.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# serving media folder in development environment
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )

