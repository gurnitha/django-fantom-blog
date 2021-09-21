# posts/views.py

# Django modules
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
		TemplateView, 
        ListView,
		DetailView, 
        CreateView)
from .forms import PostCreationForm
from django.utils.decorators import method_decorator
from django.template.defaultfilters import slugify
from django.urls import reverse

# Loclas
from .models import Post, Category, Tag

# Create your views here.

# Class:IndexView
class IndexView(ListView):
    model = Post
    context_object_name = 'posts'    
    template_name = "posts/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['slider_posts'] = Post.objects.all().filter(slider_post=True)
        return context


# Class:PostDetail
class PostDetail(DetailView):
    model = Post
    context_object_name = 'single'    
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        return context


# Class:CategoryDetail
class PostsByCategory(ListView):
    model = Post
    context_object_name = 'postsbycategory'
    template_name = 'posts/posts_by_category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category,pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(PostsByCategory, self).get_context_data(**kwargs)
        self.category = get_object_or_404(Category,pk=self.kwargs['pk'])
        context['category'] = self.category
        return context


# Class:PostsByTag
class PostsByTag(ListView):
    model = Post
    context_object_name = 'postsbytag'
    template_name = 'posts/posts_by_tag.html'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag,slug=self.kwargs['slug'])
        return Post.objects.filter(tag=self.tag).order_by('id')

    def get_context_data(self,**kwargs):
        context = super(PostsByTag, self).get_context_data(**kwargs)
        self.tag = get_object_or_404(Tag,slug=self.kwargs['slug'])
        context['tag'] = self.tag
        return context


# Class:CreatePostView
    """
    1. We have created posts with tags, but from the admin panel
    2. Now we will create post with tag(s) from the form.
    3. To create a post and tag(s), user MUST be logged in.
       un-logged in user, can NOT create post and tag(s)
    4. To do so, we have to create class of CreatePostView with
       login_required and decorator.
    5. In this scenario, form has been created. The forms has
       fields of:
       -Title
       -Content
       -Image
       -User,
       -Category,
       -Tag, and
       -Slider      

        5.1. The form fieds are based on the Post model
        5.2. But for the user and slider fields, we have 
             to find the way to manage them.

    6. There is no way to create user at the same time
       while creating a new post, therefore:
       6.1 We have created decorator with login_required (above);
       6.2 Then, add the instance of the logged in user (bellow); and 
       6.3 Save the form.

    7. Tag
       Since tag field has ManyToMany Rel, tag(s) might be already
       exist in the db, while user wanted to create more tag(s).
       Therefor we must find the way to create a new post and tag(s)
       as seen bellow(tag).  
    """

@method_decorator(login_required(login_url='users/login'),name="dispatch")
class CreatePostView(CreateView):
    template_name = 'posts/create-post.html'
    form_class = PostCreationForm
    model = Post
    
    # Return to detail page after post has been created
    def get_success_url(self):
        return reverse('detail', 
                kwargs={
                    "pk":self.object.pk,"slug":self.object.slug})

    def form_valid(self, form):
        # Saving the objects first due to ManyToMany rel in
        # the tag field in the Post model
        form.instance.user = self.request.user
        form.save()

        """
        NOTE: About the 'tags'
        1. Get the tag from the form
        2. 'Post' is the form's method, that is POST
        3. 'tag' is the name (name="tag") attribute of the form field
        4. ',' is to seperate the tag bc a post can have many tags
           ex: tag1, tag2, and tagN
        5. So, if the tag(s) not exist 'if current_tag.count()<1:', 
           then create tag(s)
        """
        tags = self.request.POST.get("tag").split(",")

        for tag in tags:
            current_tag = Tag.objects.filter(slug=slugify(tag))
            # If tag(s) not exist, create tag
            if current_tag.count()<1:
                create_tag = Tag.objects.create(title=tag) # title is the model field
                form.instance.tag.add(create_tag)

            # If tag exist, get it/them to be the instance of the form 
            else:
                existed_tag = Tag.objects.get(slug=slugify(tag))
                form.instance.tag.add(existed_tag)

        return super(CreatePostView, self).form_valid(form)

