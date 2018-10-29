from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .models import Album
from .serializers import AlbumSerializer


class AlbumView(APIView):

    def get(self, request):
        if self.request.version == '1.0':
            if 'musics' in cache:
                # from cache get musics
                album = cache.get('musics')
            else:
                album = Album.objects.all()
                serializer = AlbumSerializer(album, many=True)
                album = serializer.data
                # store data to cache
                cache.set('album', album, timeout=None)
        else:
            album = Album.objects.all()
            serializer = AlbumSerializer(album, many=True)
            album = serializer.data
        return Response(album, status=status.HTTP_200_OK)

    def post(self):
        pass

# class DetailView(generic.DetailView):
#     model = Album
#     template_name = 'recommend/detail.html'


def show_album(request, *args, **kwargs):
    return render(request, "recommend/album.html", locals())
