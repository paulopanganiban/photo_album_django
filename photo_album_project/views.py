from django.http.response import HttpResponse
from django.shortcuts import render
import json
from photo_album_project.photos.models import Post
from django.views.generic import ListView, DetailView
# Make django know in the settings.py regarding the template file
# TEMPLATES = [
    # {
    #     'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #     'DIRS': [BASE_DIR / 'templates'], <-----------

def homepage(request):
    return render(request, 'index/homepage.html')

def about(request):
    # request has the information about the request made by the user
    return render(request, 'about.html')

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name= 'index/homepage.html'
    # <app>/<model>_<viewtype>.html
    context_object_name = 'photos'

   

class PostDetailView(DetailView):
    model = Post
    template_name = 'index/detail.html'
