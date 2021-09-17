# posts/urls.py

# Django modules
from django.urls import path

# Locals
from . import views  

# Name of the app
app_name = 'posts'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index')    
] 