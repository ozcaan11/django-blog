from django.db import models
from django.db.models.signals import pre_save

from blog.utils import unique_slug_generator


class Setting(models.Model):
    header = models.CharField(max_length=120, null=True, blank=True)
    sub_header = models.CharField(max_length=120, null=True, blank=True)
    biography = models.TextField()
    bottom_message = models.TextField(null=True, blank=True)
    corner = models.TextField()

    def __str__(self):
        return self.header


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    tag = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Post)
