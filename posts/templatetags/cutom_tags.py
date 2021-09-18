# post/templatestags/custom_tags.py

# Django modules
from django import template

# Locals
from posts.models import Category, Tag


# Register template Library module of the template
register = template.Library()

# Customtag: category
@register.simple_tag(name="categories")
def all_categories():
	return Category.objects.all()

# Customtag: tag
@register.simple_tag(name="tags")
def all_tags():
	return Tag.objects.all()

