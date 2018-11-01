from rest_framework import serializers
from .models import Album
from .models import Song


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'title', 'logo', 'likes', 'watched', 'created_by')


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('album', 'video_id', 'song_title')

