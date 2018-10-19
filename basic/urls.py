from django.conf.urls import url
from django.urls import path
from basic import views

app_name = 'basic'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/', views.UserFormView.as_view(), name='register'),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^privacy/', views.privacy, name="privacy"),
]