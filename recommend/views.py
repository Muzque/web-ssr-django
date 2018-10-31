from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .models import Album
from .models import Song
from .serializers import AlbumSerializer
from .serializers import SongSerializer


class AlbumView(APIView):

    def get(self, request):
        if self.request.version == '1.0':
            if 'albums' in cache:
                # from cache get musics
                albums = cache.get('albums')
            else:
                albums = Album.objects.all()
                serializer = AlbumSerializer(albums, many=True)
                albums = serializer.data
                # store data to cache
                cache.set('albums', albums, timeout=None)
        else:
            albums = Album.objects.all()
            serializer = AlbumSerializer(albums, many=True)
            albums = serializer.data
        return Response(albums, status=status.HTTP_200_OK)

    def post(self):
        pass


class DetailView(APIView):

    def get_object(self, pk):
        try:
            return Song.objects.filter(album=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        songs = self.get_object(pk)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass


def show_album(request, *args, **kwargs):
    return render(request, "recommend/album.html", locals())


def show_detail(request, *args, **kwargs):
    return render(request, "recommend/detail.html", locals())
