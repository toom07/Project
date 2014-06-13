# Import django modules
from django.conf.urls.defaults import *


urlpatterns = patterns('waypoints.views',
    url(r'^$', 'index', name='waypoints-index'),
    url(r'^search$', 'search', name='waypoints-search'),
)
