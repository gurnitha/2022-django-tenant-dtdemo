# dtdemo/urls_public.py

# Django modules
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
