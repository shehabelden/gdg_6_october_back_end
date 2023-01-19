from .models import *
from django.db.models.signals import post_save, pre_delete


def create(sender, instance, created, **kwargs):
    if created:
        BlogModel.objects.create(user=instance.user, title=instance.title, image=instance.image, topic="blog")


post_save.connect(create, sender=BlogModel)


def create(sender, instance, created, **kwargs):
    if created:
        MainBlogModel.objects.create(user=instance.user, title=instance.name, image=instance.image, topic="blog")


post_save.connect(create, sender=MainBlogModel)
