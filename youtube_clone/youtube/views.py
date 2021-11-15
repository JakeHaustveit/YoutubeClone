from django.http.response import Http404
from rest_framework import response
from rest_framework.serializers import Serializer
from .models import Comment, Reply
from .serializers import CommentSerializer, ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CommentList(APIView):

    

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentForVideo(APIView):   

    def get(self, request, id):
        
        comment = Comment.objects.filter(video_id=id)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)


class ReplyForComment(APIView):

    def get(self, request, id):
        comment_reply= Reply.objects.filter(comment_id=id)
        serializer = ReplySerializer(comment_reply, many=True)
        return Response(serializer.data)



class CommentDetail(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReplyList(APIView):

    def get(self, request):
        reply = Reply.objects.all()
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReplyDetail(APIView):

    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reply = self.get_object(pk)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)
    
    def put(self, request, pk):
        reply = self.get_object(pk)
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reply = self.get_object(pk)
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentLikes(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        comment.likes += 1
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

class CommentDislikes(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        comment.dislikes += 1
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)