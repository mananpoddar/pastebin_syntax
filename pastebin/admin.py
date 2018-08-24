from django.contrib import admin
from pastebin.models import paste,User,paste_logged_in

admin.site.register(paste)
admin.site.register(paste_logged_in)