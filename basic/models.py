from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    nickname = models.CharField(blank=True, null=True, max_length=15, default=None)
    user_img = models.FileField(upload_to='user_img', default=None)
    belong_to = models.OneToOneField(to=User, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.belong_to.username)


class AppInfo(models.Model):
    appname = models.CharField(null=False, max_length=20)
    content = models.TextField()

    def __str__(self):
        return str(self.appname)


class Comment(models.Model):
    avatar = models.ForeignKey(null=True, blank=True, to=UserProfile,
                               related_name='comment_avatar', on_delete=models.CASCADE)
    name = models.ForeignKey(null=True, to=User, related_name='comment_name', on_delete=models.CASCADE)
    comment = models.TextField(null=False, blank=False)
    submit_time = models.DateTimeField(default=timezone.now)
    belong_to = models.ForeignKey(null=True, blank=True, to=AppInfo,
                                  related_name='under_comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment.encode('utf-8')
