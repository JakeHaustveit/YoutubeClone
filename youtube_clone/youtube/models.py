from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Comment(models.Model):
    text= models.CharField(max_length=400)
    likes= models.IntegerField(default=0)    
    dislikes= models.IntegerField(default=0)

class VideoComment(models.Model):
    comment= models.CharField(max_length=400)
    comment_on_comment= models.ForeignKey(CommentonComment, on_delete=models.CASCADE)


class Video(models.Model):
    videoId= models.CharField(max_length=400)
    




    

