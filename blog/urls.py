from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', single_view, name='single'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('tags/<str:tag_name>', blog_view, name='tag'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('search/', blog_search, name='search'), #it is necessary to have the final slash, same as the below test call
    path('test/', test) #it is necessary to have a '/' in the end, as it shows this slash in the URL section of the page
]