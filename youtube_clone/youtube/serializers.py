from django.db.models import fields
from rest_framework import serializers
from .models import Comment, Reply


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'likes', 'videoId', 'dislikes']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['text', 'comment']
     