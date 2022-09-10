from django.db import models
from django.contrib.auth.models import User


class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    urls = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(editable=False, auto_now_add=True)
    token = models.CharField(max_length=255, blank=False)


class guest(models.Model):
    urls = models.CharField(max_length=255)
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=6, unique=True)
