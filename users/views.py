# users/forms.py

# Django modules
from django.shortcuts import render
from django.views.generic import CreateView

# Locals
from users.forms import RegisterForm

# Create your views here.

# Class:RegisterView
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = '/'