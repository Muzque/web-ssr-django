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


class Playlist(APIView):
    authentication_classes = [] #(authentication.TokenAuthentication,)
    permission_classes = [] #(permissions.IsAdminUser,)

    def __init__(self, *args, **kwargs):
        super(Playlist, self).__init__(*args, **kwargs)
        self.cfg = ConfigParser()
        self.cfg.read('envs.cfg')

    def get(self, request, format=None):
        key = self.cfg.get("Google_Youtube", "APIkey")
        query = request.GET.get("query")
        url_channelId = "https://www.googleapis.com/youtube/v3/channels?key={}" \
                        "&part=snippet&forUsername={}".format(key, query)
        res = requests.get(url=url_channelId).json()
        channelId = res['items'][0]['id']
        url_playlist = "https://www.googleapis.com/youtube/v3/playlists?key={}" \
                       "&part=snippet,contentDetails&maxResults=50&channelId={}".format(key, channelId)
        res = requests.get(url=url_playlist).json()
        # url_play = 'https://www.youtube.com/playlist?list='
        data = list()
        for line in res['items']:
            data.append({
                'img': line['snippet']['thumbnails']['medium']['url'],
                'title': line['snippet']['title'],
                'publishedAt': line['snippet']['publishedAt'],
                'playlistId': line['id']
            })
        return Response(data)


class Listen(APIView):
    authentication_classes = [] #(authentication.TokenAuthentication,)
    permission_classes = [] #(permissions.IsAdminUser,)

    def __init__(self, *args, **kwargs):
        super(Listen, self).__init__(*args, **kwargs)
        self.cfg = ConfigParser()
        self.cfg.read('envs.cfg')

    def get(self, request, format=None):
        key = self.cfg.get("Google_Youtube", "APIkey")
        playlistId = request.GET.get('playlistId')
        url = "https://www.googleapis.com/youtube/v3/playlistItems?key={}" \
              "&part=snippet&maxResults=50&playlistId={}".format(key, playlistId)
        res = requests.get(url=url).json()
        data = list()
        for line in res['items']:
            data.append({
                'title': line['snippet']['title'],
                'videoId': line['snippet']['resourceId']['videoId']
            })
        return Response(data)


def show_youtube(request):
    return render(request, "youtube/youtube.html", locals())
