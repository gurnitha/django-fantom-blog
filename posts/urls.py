# posts/urls.py

# Django modules
from django.urls import path

# Locals
from . import views  

# Name of the app
# app_name = 'posts'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/<slug:slug>/', views.PostDetail.as_view(),name="detail"),    
    path('category/<int:pk>/<slug:slug>', views.PostsByCategory.as_view(),name="posts_by_category"),
    path('tags/<int:pk>/<slug:slug>/', views.PostsByTag.as_view(),name="posts_by_tag"),
    path('post-create/', views.CreatePostView.as_view(),name="create_post"),

] 