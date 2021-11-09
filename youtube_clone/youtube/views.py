from django.http.response import Http404
from rest_framework import response
from rest_framework.serializers import Serializer
from .models import Comment, Reply
from .serializers import CommentSerializer, ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
