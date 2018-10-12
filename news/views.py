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


class News(APIView):
    authentication_classes = [] #(authentication.TokenAuthentication,)
    permission_classes = [] #(permissions.IsAdminUser,)

    def __init__(self, *args, **kwargs):
        super(News, self).__init__(*args, **kwargs)
        self.cfg = ConfigParser()
        self.cfg.read('private/envs.cfg')

    def get(self, request, format=None):
        key = self.cfg.get("News", "APIkey")
        queryset = request.GET.get("search")
        url = 'https://newsapi.org/v2/everything?q={}&apiKey={}&sortBy={}'.format(queryset, key, "relevancy")
        res = requests.get(url=url).json()
        data = list()
        for line in res['articles']:
            data.append({
                'link': line['url'],
                'img': line['urlToImage'],
                'title': line['title'],
                'description': line['description'],
                'author': line['author'],
                'publishedAt': line['publishedAt'],
                'content': line['content']
            })
        return Response(data)


def show_news(request):
    return render(request, "news/news.html", locals())
