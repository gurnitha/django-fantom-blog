# posts/admin.py

# Django modules
from django.contrib import admin

# Locals
from .models import Post

# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_filter = ['publishing_date']
    list_display = ['title','publishing_date']
    search_fields = ['title','content']

    class Meta:
    	model = Post 


admin.site.register(Post,AdminPost)