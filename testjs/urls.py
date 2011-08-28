from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('testjs.views',
    url(r'^(?P<test_name>\w+)/$', 'run_test'),
)
