from django.db.models import fields
from rest_framework import serializers
from .models import CommentonComment, VideoComment, Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [' videoId', 'likes', 'video_comment', 'dislikes']

class VideoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [' videoId', 'likes', 'video_comment', 'dislikes']

class CommentonCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['comment']        