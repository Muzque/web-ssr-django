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


class Weather(APIView):
    authentication_classes = [] #(BasicAuthentication, SessionAuthentication)
    permission_classes = [] #(IsAdminUser,)

    def __init__(self, *args, **kwargs):
        super(Weather, self).__init__(*args, **kwargs)
        self.cfg = ConfigParser()
        self.cfg.read('envs.cfg')

    def get(self, request, format=None):
        city = request.GET.get('city').lower()
        key = self.cfg.get('weather', 'APIkey')
        url = 'http://api.openweathermap.org/data/2.5/forecast'
        if city is not None:
            if city == 'here':
                gkey = self.cfg.get('googlemap', 'APIkey')
                gurl = 'https://www.googleapis.com/geolocation/v1/geolocate?key='
                res = requests.post(gurl+gkey).json()
                lat = res['location']['lat']
                lon = res['location']['lng']
                url = url + '?lat={}&lon={}&units=metric'.format(lat, lon)
            else:
                url = url + '?q={}&units=metric'.format(city)
        url = url + '&APPID={}'.format(key)
        res = requests.get(url).json()
        ls_res = res['list']
        data = list()
        for line in ls_res:
            data.append({
                'datetime': datetime.datetime.fromtimestamp(int(line['dt'])),
                'weather': line['weather'][0]['description'],
                'temp': line['main']['temp'],
                'pressure': line['main']['pressure'],
                'humidity': line['main']['humidity']
            })
        return Response(data=data)


def show_weather(request):
    return render(request, "weather/weather.html", locals())
