from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Comment(models.Model):
    text = models.CharField(max_length=400)
    video_id= models.CharField(max_length=400)
    likes= models.IntegerField(default=0, )
    dislikes= models.IntegerField(default=0, )

class Reply(models.Model):
    text = models.CharField(max_length=400)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)






    

