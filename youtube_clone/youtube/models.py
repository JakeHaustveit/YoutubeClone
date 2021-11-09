from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class CommentonComment(models.Model):
    comment= models.CharField(max_length=400)

class VideoComment(models.Model):
    comment= models.CharField(max_length=400)
    comment_on_comment= models.ForeignKey(CommentonComment, on_delete=models.CASCADE)


class Video(models.Model):
    videoId= models.CharField(max_length=400)
    likes= models.IntegerField(default=0)
    video_comment= models.ForeignKey(VideoComment, on_delete=models.CASCADE)
    dislikes= models.IntegerField(default=0)




    

