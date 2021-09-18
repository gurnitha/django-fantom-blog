# users/urls.py

# Django modules
from django.urls import path

# Locals
from . import views  

app_name = 'users'

urlpatterns = [
	path('register/', views.RegisterView.as_view(), name='register')
] 