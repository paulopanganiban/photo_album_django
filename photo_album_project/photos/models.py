from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.

#class Photo(models.Model):
    #owner - current logged in user
    #name
    #imageField
    #date uploaded
    #views
    #downloads
    #categories
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='photo_gallery')
    def __str__(self):
        return self.title