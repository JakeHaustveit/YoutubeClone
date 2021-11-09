from django.db import models

# Create your models here.
class Video(models.Model):
    videoId= models.IntegerField()
    likes= models.IntegerField(default=0)
    comment= models.ForeignKey.CharField(max_length=400)
    dislikes= models.IntegerField(default=0)



class VideoComment(models.Model):
    comment= models.ForeignKey.CharField(max_length=400)
    

class CommentonComment(models.Model):
    comment= models.CharField(max_length=400)