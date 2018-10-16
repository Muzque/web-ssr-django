from django.conf.urls import url
from django.urls import path
from news import views

app_name = 'news'
urlpatterns = [
    url(r'^$', views.show_news, name="index"),
    url(r'^api/', views.News.as_view()),
]