from django.conf.urls import url, include
from django.contrib import admin
from karrata.views import *

urlpatterns = [

    url(r'^login/$', login, name='login' ),
    url(r'^logout/$', logout, name='logout'),
    url(r'^loggedin/$', loggedin, name='loggedin'),
    url(r'^register/$', register , name='register'),
    url(r'^auth/$', register_auth, name='register-now'),
    url(r'^success/$', register_success),
    url(r'^invalid/$', invalid_login, name='invalid'),

]