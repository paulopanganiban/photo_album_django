from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
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
    title = models.CharField("Name of post", max_length=50)
    slug = AutoSlugField("Photo Address", unique=True, populate_from="title")
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='photo_gallery')
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('photos:detail', kwargs={'slug': self.slug})