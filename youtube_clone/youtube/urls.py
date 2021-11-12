from django.http import request
from django.urls import path
from . import views


urlpatterns = [
    path('comment/', views.CommentList.as_view()),
    path('videocomment/<str:id>/', views.CommentForVideo.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    path('reply/', views.ReplyList.as_view()),
    path('comment/<int:pk>/likes/', views.CommentLikes.as_view()),
    path('comment/<int:pk>/dislikes/', views.CommentDislikes.as_view())

]