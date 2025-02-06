from django.conf.urls import re_path
from module import views

urlpatterns = [
    re_path('module', views.module),
    ]