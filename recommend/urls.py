from django.conf.urls import url
from django.urls import path
from recommend import views

app_name = 'recommend'
urlpatterns = [
    url(r'^api/album/$', views.AlbumView.as_view(), name="api_album"),
    url(r'^$', views.show_album, name="index"),
    url(r'^api/songs/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='api_detail'),
    url(r'^songs/$', views.show_detail, name='detail'),
]