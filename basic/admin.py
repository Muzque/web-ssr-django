from django.contrib import admin
from .models import UserProfile
from .models import AppInfo
from .models import Comment

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(AppInfo)
admin.site.register(Comment)
