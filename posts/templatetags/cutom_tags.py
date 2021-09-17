# post/templatestags/custom_tags.py

# Django modules
from django import template

# Locals
from posts.models import Category


# Register template Library module of the template
register = template.Library()

@register.simple_tag(name="categories")
def all_categories():
	return Category.objects.all()

