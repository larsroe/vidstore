from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    #Main page, shows list of videos to rent
    (r'^main/$', 'vidstore.video.views.listall'),

    #Detail view about a specific video
    (r'^viddetail/(?P<video_id>\d+)/$', 'vidstore.video.views.detail'),

    #Check out/return
    (r'^rent/$', 'vidstore.video.views.rent'),

    #Log in/out
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
