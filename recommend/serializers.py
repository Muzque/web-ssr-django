from rest_framework import serializers
from .models import Album
# from .models import Song


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        field = ('title', 'logo', 'likes', 'watched', 'created_by')

