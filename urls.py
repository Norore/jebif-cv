from django.conf.urls import *
from django.contrib import admin

from jebif import settings

urlpatterns = patterns('',
    (r'^cv/',           include('cv.candidate.urls')),
    (r'^users/',        include('cv.users.urls')),
    (r'^accounts/',     include('cv.registration.urls')),
)
urlpatterns += patterns('django.views.generic.simple',
    # Homepage
    (r'', 'direct_to_template', {'template': 'homepage.html'}),
)

