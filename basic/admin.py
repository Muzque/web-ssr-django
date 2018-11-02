from django.contrib import admin
from django.contrib.auth.models import User
from configparser import ConfigParser
from .models import UserProfile
from .models import AppInfo
from .models import Comment

# Create superuser
cfg = ConfigParser()
cfg.read('private/envs.cfg')
User.objects.create_superuser(username=cfg.get('Model', 'SUPERUSER_ROOT'),
                              password=cfg.get('Model', 'SUPERUSER_PASSWORD'),
                              email=cfg.get('Model', 'SUPERUSER_EMAIL'))

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(AppInfo)
admin.site.register(Comment)
