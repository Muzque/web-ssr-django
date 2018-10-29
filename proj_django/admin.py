from django.contrib import admin
from recommend.models import Album
from recommend.models import Song

# Register your models here.
admin.site.register(Album)
admin.site.register(Song)