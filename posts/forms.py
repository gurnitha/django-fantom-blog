# posts/forms.py

# Django modules
from django import forms

# Locals
from . models import *


# Class:PostCreationForm
class PostCreationForm(foms.ModelForm):

	class Meta:
		model = Post

	# Refer to Post model's fields
	fields = [
		'title',
		'category',
		'content', 
		'image',
		'tag'
	]

