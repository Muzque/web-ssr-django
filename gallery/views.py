from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from configparser import ConfigParser
import requests
import datetime


class Gallery(APIView):
    authentication_classes = [] #(authentication.TokenAuthentication,)
    permission_classes = [] #(permissions.IsAdminUser,)

    def __init__(self, *args, **kwargs):
        super(Gallery, self).__init__(*args, **kwargs)
        self.cfg = ConfigParser()
        self.cfg.read('envs.cfg')

    def get(self, request, format=None):
        key = self.cfg.get("Unsplash", "APIkey")
        page = request.GET.get("page")
        url = 'https://api.unsplash.com/photos/?client_id={}&per_page=30&page={}'.format(key, page)
        res = requests.get(url=url).json()
        data = list()
        for line in res:
            data.append({
                'img': line['urls']['small'],
                'profile_image': line['user']['profile_image']['small'],
                'author': line['user']['username'],
                'location': line['user']['location'],
                'likes': line['likes']
            })
        return Response(data)


def show_gallery(request):
    return render(request, "gallery/gallery.html", locals())
