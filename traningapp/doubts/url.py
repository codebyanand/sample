from django.conf.urls import re_path
from doubts import views

urlpatterns = [
    re_path('adddb/', views.doubt),
]