from django.db import models
from time import time
# Create your models here.

def get_upload_file_name(instance, filename):
    return "media/%s_%s" % (str(time()).replace('.','_'), filename)

class Article(models.Model):
    title = models.CharField(max_length=254)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to=get_upload_file_name)
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.ForeignKey(Article)
    body = models.TextField()

    def __str__(self):
        return "%s | Numero de Likes: %s " % (self.article , str(self.article.likes))
