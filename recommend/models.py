from django.db import models


class Album(models.Model):
    title = models.CharField(null=False, max_length=20)
    logo = models.TextField(null=False)
    likes = models.IntegerField(default=0)
    watched = models.IntegerField(default=0)
    created_by = models.CharField(null=False, max_length=20)

    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    video_id = models.CharField(null=False, max_length=20)
    song_title = models.CharField(null=True, max_length=64)



