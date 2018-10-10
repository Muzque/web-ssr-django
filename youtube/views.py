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


def show_youtube(request):
    return render(request, "youtube/youtube.html", locals())
