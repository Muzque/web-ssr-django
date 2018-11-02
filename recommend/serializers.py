from rest_framework import serializers
from basic.models import UserProfile
from .models import Album
from .models import Song


class AlbumSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source='created_by.profile.nickname')
    if creator == '':
        creator = serializers.CharField(source='created_by.username')
    avatar = serializers.ImageField(source='created_by.profile.user_img')

    class Meta:
        model = Album
        fields = ('id', 'title', 'logo', 'likes', 'watched', 'creator', 'avatar')


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id', 'album', 'video_id', 'song_title')

