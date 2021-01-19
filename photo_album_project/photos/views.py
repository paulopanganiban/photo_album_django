from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
    )
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


def dashboard(request):
    context = {
        'photos': Post.objects.all()
    }
    return render(request, 'photos/dashboard.html', context)


class PostDashboardListView(ListView):
    model = Post
    template_name = 'photos/dashboard.html'
    context_object_name = 'photos'
    def get_queryset(self):
        return Post.objects.filter(author_id=self.request.user)
    

class PostDashboardDetailView(DetailView):
    model = Post
    template_name = 'photos/detail.html'

class PostDashboardCreateView(CreateView):
    model = Post
    fields = ['title', 'image']

    def form_valid(self, form):
        form.instance.author = self.request
        return super().form_valid(form)