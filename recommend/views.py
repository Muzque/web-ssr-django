from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Album
from .serializers import AlbumSerializer


class AlbumView(APIView):

    def get(self, request):
        album = Album.objects.all()
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self):
        pass

# class DetailView(generic.DetailView):
#     model = Album
#     template_name = 'recommend/detail.html'

