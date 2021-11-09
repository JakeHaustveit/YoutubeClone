from django.contrib import admin
from .models import CommentonComment, VideoComment, Video

# Register your models here.
admin.site.register(CommentonComment, VideoComment, Video)