from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class paste(models.Model):
    content = HTMLField(max_length=1000000)
    url = models.AutoField(primary_key=True)
class paste_logged_in(models.Model):
    content = models.TextField(max_length=1000000)
    url = models.AutoField(primary_key=True)
    owner=models.CharField(blank=True,max_length=60)