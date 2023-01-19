from django.db import models
from django.contrib.auth.models import User
class TeamModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=40,default="s")
    bio = models.CharField(max_length=4000)
