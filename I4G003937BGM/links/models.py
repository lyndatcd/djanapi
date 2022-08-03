from django.db import models
from django.contrib.auth import get_user_model

from .managers import ActiveLinkManager

User = get_user_model()


# Create your models here.

class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(null=True, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public = ActiveLinkManager()

    def __str__(self):
        return self.target_url
