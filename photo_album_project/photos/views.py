from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import TestModelForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalFormView, BSModalReadView
from django.urls import reverse_lazy
from hitcount.views import HitCountDetailView
# Create your views here.
import os
from django.conf import settings
from django.http import HttpResponse, Http404

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="image/jpeg")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

# test bs modal form

class TestReadView(BSModalReadView):
    model = Post
    template_name = 'photos/test.html'

def dashboard(request):
    context = {
        'photos': Post.objects.all()
    }
    return render(request, 'photos/dashboard.html', context)

class PostDashboardListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'photos/dashboard.html'
    context_object_name = 'photos'
    
    def get_queryset(self):
        return Post.objects.filter(author_id=self.request.user)
    

class PostDashboardDetailView(DetailView):
    model = Post
    template_name = 'photos/detail.html'

class PostDashboardCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDashboardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image']

    def form_valid(self, form):
        
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDashboardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self): # check if the post is currently by the logged in user
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False