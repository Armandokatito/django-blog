from django.conf.urls import url
from article.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^all/$', articles, name='all'),
    url(r'^create/$', create, name='create'),
    url(r'^get/(?P<article_id>\d+)/$', article, name='get' ),
    url(r'^language/(?P<lang>[a-zA-Z\-]+)/$', language, name='language' ),
    url(r'^like/(?P<article_id>\d+)/$', like_article, name="likes"),
    url(r'^add_comment/(?P<article_id>\d+)/$', add_comment, name='comment'),
    url(r'^search/$', search_tile, name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)