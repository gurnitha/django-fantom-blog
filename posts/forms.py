# posts/forms.py

# Django modules
from django import forms

# Locals
from . models import *


# Class:PostCreationForm
class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets = {
            'title':forms.TextInput(attrs={
            				'class':'single-input',
            				'placeholder':'Enter your title'}),
            'content':forms.Textarea(attrs={
            				'class':'single-input',
            				'placeholder':'Enter your content'}),
        }

        fields = [
            'title',
            'category',
            'content',
            'image',

        ]
