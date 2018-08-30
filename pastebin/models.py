from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from datetime import timezone



class paste(models.Model):
    content = RichTextField(max_length=1000000)
    url = models.AutoField(primary_key=True)
    expiration_date= models.DateField(blank=True, null=True)
    editable = models.BooleanField(default=False)
class paste_logged_in(models.Model):
    content = models.TextField(max_length=1000000)
    url = models.AutoField(primary_key=True)
    owner=models.CharField(blank=True,max_length=60)
    expiration_date= models.DateField(blank=True, null=True)
    editable = models.BooleanField(default=False)

