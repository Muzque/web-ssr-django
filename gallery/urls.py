from django.conf.urls import url
from django.urls import path
from gallery import views

app_name = 'gallery'
urlpatterns = [
    url(r'api/', views.Gallery.as_view()),
    url(r'^', views.show_gallery, name="index"),
]