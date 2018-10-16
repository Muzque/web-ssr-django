from django.conf.urls import url
from django.urls import path
from youtube import views

app_name = 'youtube'
urlpatterns = [
    url(r'^api/playlist/', views.Playlist.as_view()),
    url(r'^api/listen/', views.Listen.as_view()),
    url(r'^$', views.show_youtube, name="index"),
]