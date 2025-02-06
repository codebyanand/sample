from django.conf.urls import re_path
from feedback import views

urlpatterns = [
    re_path('feedback/', views.feedback),
    ]