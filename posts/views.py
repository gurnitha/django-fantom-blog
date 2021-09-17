# posts/views.py

# Django modules
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Class:
class IndexView(TemplateView):
	template_name = 'posts/index.html'
