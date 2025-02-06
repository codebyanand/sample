from django.conf.urls import re_path
from student import views

urlpatterns = [
    re_path('reg/', views.register),
    re_path('log/',views.login)
]