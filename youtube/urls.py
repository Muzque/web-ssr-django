from django.conf.urls import url
from django.urls import path
from youtube import views

app_name = 'youtube'
urlpatterns = [
    url(r'^$', views.show_youtube, name="index"),
]