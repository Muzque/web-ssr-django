from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from configparser import ConfigParser


class Weather(APIView):

    def get(self, request, format=None):
        cfg = ConfigParser().read('envs.cfg')['weather']
        url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={}'.format(cfg['APIkey'])
