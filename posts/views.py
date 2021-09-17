# posts/views.py

# Django modules
from django.shortcuts import render
from django.views.generic import (
		TemplateView, ListView,
		DetailView)

# Loclas
from .models import Post 

# Create your views here.

# Class:IndexView
class IndexView(ListView):
    model = Post
    context_object_name = 'posts'    
    template_name = "posts/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


# Class:PostDetail
class PostDetail(DetailView):
    model = Post
    context_object_name = 'single'    
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        return context