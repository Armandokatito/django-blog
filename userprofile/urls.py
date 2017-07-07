from django.conf.urls import url, include
from userprofile.views import *

urlpatterns = [

    url(r'^profile/$', user_profile, name='profile' ),

]