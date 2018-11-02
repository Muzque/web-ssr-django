from rest_framework import serializers
from .models import Album
from .models import Song


class AlbumSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source='created_by.username')

    class Meta:
        model = Album
        fields = ('id', 'title', 'logo', 'likes', 'watched', 'creator')


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id', 'album', 'video_id', 'song_title')

