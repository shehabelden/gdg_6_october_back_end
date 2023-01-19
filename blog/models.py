from django.db import models
from django.contrib.auth.models import User


class BlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.FileField()
    image = models.ImageField()
    title = models.CharField(max_length=40,)


class MainBlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=40,)
    blog = models.ManyToManyField("BlogModel")
