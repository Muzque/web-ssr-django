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
                albums = cache.get('albums')
            else:
                albums = Album.objects.all()
                serializer = AlbumSerializer(albums, many=True)
                albums = serializer.data
                cache.set('albums', albums, timeout=None)
        else:
            albums = Album.objects.all()
            serializer = AlbumSerializer(albums, many=True)
            albums = serializer.data
        return Response(albums, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        album = self.get_object(pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        album = self.get_object(pk)
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        album = self.get_object(pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongView(APIView):

    def get(self, request):
        if self.request.version == '1.0':
            if 'songs' in cache:
                songs = cache.get('songs')
            else:
                songs = Song.objects.all()
                serializer = SongSerializer(songs, many=True)
                songs = serializer.data
                cache.set('songs', songs, timeout=None)
        else:
            songs = Song.objects.all()
            serializer = SongSerializer(songs, many=True)
            songs = serializer.data
        return Response(songs, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        song = self.get_object(pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumFilter(APIView):

    def get_object(self, pk):
        try:
            return Song.objects.filter(album=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        songs = self.get_object(pk)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def show_album(request, *args, **kwargs):
    return render(request, "recommend/album.html", locals())


def show_detail(request, *args, **kwargs):
    return render(request, "recommend/detail.html", locals())
