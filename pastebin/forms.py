from django import forms
from django.core import validators
from pastebin.models import paste,User,paste_logged_in
from django.db import models



class input(forms.ModelForm):
    url = models.AutoField(primary_key=True)
    class Meta:
        model = paste
        fields= '__all__'

class input_logged_in(forms.ModelForm):
    url = models.AutoField(primary_key=True)
    class Meta:
        model = paste_logged_in
        fields= '__all__'


class Authentic(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields =("username","password","first_name","last_name","email",)

