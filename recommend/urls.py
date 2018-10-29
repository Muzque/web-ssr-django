from django.conf.urls import url
from django.urls import path
from recommend import views

app_name = 'recommend'
urlpatterns = [
    url(r'^api/$', views.AlbumView.as_view(), name="index"),
    url(r'^$', views.show_album, name="index"),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]