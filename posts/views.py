# posts/views.py

# Django modules
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
		TemplateView, ListView,
		DetailView)

# Loclas
from .models import Post, Category, Tag

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


# Class:CategoryDetail
class PostsByCategory(ListView):
    model = Post
    context_object_name = 'postsbycategory'
    template_name = 'posts/posts_by_category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category,pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(PostsByCategory, self).get_context_data(**kwargs)
        self.category = get_object_or_404(Category,pk=self.kwargs['pk'])
        context['category'] = self.category
        return context


# Class:PostsByTag
class PostsByTag(ListView):
    model = Post
    context_object_name = 'postsbytag'
    template_name = 'posts/posts_by_tag.html'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag,slug=self.kwargs['slug'])
        return Post.objects.filter(tag=self.tag).order_by('id')

    def get_context_data(self,**kwargs):
        context = super(PostsByTag, self).get_context_data(**kwargs)
        self.tag = get_object_or_404(Tag,slug=self.kwargs['slug'])
        context['tag'] = self.tag
        return context

