
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^pastebin/', include("pastebin.urls" , namespace="pastebin")),
    url(r'^tinymce/', include('tinymce.urls')),



]
