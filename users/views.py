# users/forms.py

# Django modules
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

# Locals
from users.forms import RegisterForm

# Create your views here.

# Class:RegisterView
class RegisterView(CreateView):
    # Note: order of 1,2, and 3 is metter
    template_name = 'users/register.html' #1
    form_class = RegisterForm #2
    success_url = '/' #3


# Class:UserLoginView
class UserLoginView(LoginView):
    template_name = 'users/login.html'

