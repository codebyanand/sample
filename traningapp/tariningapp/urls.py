"""tariningapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from course import views as co
from doubts import views as do
from feedback import views as fe
from module import views as mo
from request import views as re
from student import  views as st
from teacher import views as tv
from mainpage import views as mi
from login import views as lg
urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/',co.course),
    path('view/', co.view),
    path('doubts/',do.doubt),
    path('studentdoubt/',do.respons),
    path('feedback/',fe.feedback),
    path('viewfeedback/',fe.viewfeedback),
    path('module/',mo.module),
    path('viewmodule/',mo.viewmodule),
    path('login/',lg.login),
    path('register/',st.register),
    path('studentpage/',st.mainpage),
    path('st_main/',st.student_mainpage),
    path('teacherpage/',tv.techerpage),
    path('teacherslogin/',tv.teacher_mainpage),
    path('teachersreg/',tv.techerpage),
    path('techmain/', tv.teacher_main),
    url('$', mi.user),
    url('main/', mi.user),



]
