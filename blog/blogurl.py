from django.urls import path
from .api import *
urlpatterns = [
    path('MainBlog',MainBlogApi.as_view()),
    path('AllBlog', AllBlogApi.as_view()),
    path('OneBlog/<int:id>', OneBlogApi.as_view()),
]