from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.views import login, logout
#from vidstore.video.views import *

admin.autodiscover()

urlpatterns = patterns('vidstore.video.views',
    #Main page, shows list of videos to rent
    (r'^main/$', 'listall'),
    (r'^$', 'listall'),

    #Detail view about a specific video, uses database ID
    (r'^viddetail/(?P<id>\d+)/$', 'detail'),

    #Rent/return videos
    (r'^rent/$', 'rent_video'),
    (r'^return/$', 'return_video'),

    #Log in/out
    (r'^accounts/$', login),
    (r'^accounts/logout/$', logout),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
