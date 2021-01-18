from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.
def dashboard(request):
    context = {
        'photos': Post.objects.all()
    }
    return render(request, 'photos/dashboard.html', context)

class PostDashboardListView(ListView):
    model = Post
    template_name= 'photos/dashboard.html'
    # <app>/<model>_<viewtype>.html
    context_object_name = 'photos'

class PostDashboardDetailView(DetailView):
    model = Post
    template_name = 'photos/detail.html'