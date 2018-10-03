from django.conf.urls import url
from django.urls import path
from weather import views

app_name = 'weather'
urlpatterns = [
    url(r'api/', views.Weather.as_view()),
    url(r'', views.show_weather),
]
