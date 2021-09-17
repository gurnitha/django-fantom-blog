# django-fantom-blog
This is my exercise based on Django 3.0 MasterClass - Learn How To Create Django Apps on Udemy: https://www.udemy.com/course/django-30-masterclass-learn-how-to-create-django-apps/


#### 01. What We Are Going To Build?
        Pass 

#### 02. Creating Our Django Project

        modified:   .gitignore
        new file:   config/__init__.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

#### 03. Creating Templates, Static, Media folders and paths

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   static/css/_button.css
        ...
        new file:   static/css/_button.css.map
        new file:   static/css/_feature.css


#### 04. Creating 'posts' App and urls

        modified:   config/urls.py
        new file:   posts/__init__.py
        new file:   posts/admin.py
        new file:   posts/apps.py
        new file:   posts/migrations/__init__.py
        new file:   posts/models.py
        new file:   posts/tests.py
        new file:   posts/urls.py
        new file:   posts/views.py


#### 05. Creating home page: templates, views and urls

        modified:   README.md
        modified:   posts/urls.py
        modified:   posts/views.py
        new file:   templates/posts/index.html


#### 06. Loding Static Files

        modified:   README.md
        modified:   templates/posts/index.html


#### 07. Creating Base Html

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/posts/index.html


#### 08. Creating Super User

        modified:   README.md


#### 09. Register the app, creating Post model, install pillow, run migrations and register it to admin

        modified:   README.md
        modified:   config/settings.py
        modified:   posts/admin.py
        new file:   posts/migrations/0001_initial.py
        modified:   posts/models.py


#### 10. Creating Posts For Our Projects

        modified:   README.md
        new file:   media/uploads/blog-1.jpg
        new file:   media/uploads/blog-2.jpg
        new file:   media/uploads/blog-3.jpg
        new file:   media/uploads/blog-4.jpg


### 11. Using Generic Class Based View : ListView

        modified:   README.md
        modified:   posts/urls.py
        modified:   posts/views.py
        modified:   templates/posts/index.html


#### 12. Using Generic Class Based View : DetailView

        modified:   README.md
        modified:   posts/urls.py
        modified:   posts/views.py
        new file:   templates/posts/detail.html
        modified:   templates/posts/index.html


#### 13. Displaying Our Specific Post

        modified:   templates/posts/index.html

        NOTE: This must be with detail.html


#### 14. How To Use Slug Field to save post title as slug and use it in the url
     
        modified:   README.md
        new file:   posts/migrations/0002_post_slug.py
        modified:   posts/models.py
        modified:   posts/urls.py


#### 15. How To Create Category Model

        modified:   README.md
        new file:   media/uploads/blog-1_lq1zkqx.jpg
        new file:   media/uploads/blog-2_SIH9eYd.jpg
        new file:   media/uploads/blog-3_6wMFIab.jpg
        new file:   media/uploads/blog-3_94w11hP.jpg
        new file:   media/uploads/blog-4_SZ9lNSP.jpg
        modified:   posts/admin.py
        modified:   posts/migrations/0001_initial.py
        deleted:    posts/migrations/0002_post_slug.py
        modified:   posts/models.py


#### 16. How To Create Right Side Html File with include to keep DRY

        modified:   README.md
        modified:   templates/posts/detail.html
        modified:   templates/posts/index.html
        new file:   templates/posts/sight_side.html


### 17.1 Create Custom Tags and display categories

        modified:   README.md
        new file:   posts/templatetags/__init__.py
        new file:   posts/templatetags/cutom_tags.py
        modified:   templates/posts/sight_side.html


#### 17.2 Count number of posts in each category

        modified:   README.md
        modified:   posts/models.py
        modified:   templates/posts/sight_side.html































































































































