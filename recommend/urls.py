from django.conf.urls import url
from django.urls import path
from recommend import views

app_name = 'recommend'
urlpatterns = [
    url(r'^api/album/$', views.AlbumView.as_view(), name="api_album"),
    url(r'^api/album/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view(), name="api_album_detail"),
    url(r'^$', views.show_album, name="index"),
    url(r'^api/song/$', views.SongView.as_view(), name='api_song'),
    url(r'^api/song/(?P<pk>[0-9]+)/$', views.SongDetail.as_view(), name='api_song_detail'),
    url(r'^api/album/filter/(?P<pk>[0-9]+)/$', views.AlbumFilter.as_view(), name='api_album_filter'),
    url(r'^songs/$', views.show_detail, name='detail'),
]