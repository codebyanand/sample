from django.shortcuts import render
from student.models import StudentInfo, LoginInfo
from django.http import HttpResponse
from login.models import models


# Create your views here.

def register(request):
    if request.method == 'POST':
        obc = StudentInfo()
        obc.name = request.POST.get('name')
        obc.age = request.POST.get('age')
        obc.gender = request.POST.get('gender')
        obc.password = request.POST.get('Password')
        obc.address = request.POST.get('address')
        obc.phone = request.POST.get('phone')
        obc.email = request.POST.get('email')

        # Save the data
        obc.save()
        ob=LoginInfo()
        ob.user_name=obc.name
        ob.password=obc.password
        ob.user_type="student"
        ob.save()
        return HttpResponse("Registration successful.")
    return render(request, 'student/registration.html')


# def login(request):
#     return render(request, 'student/../login/templates/login/login.html')


def mainpage(request):
    return render(request, 'student/student_main_page2.html')


# def regview(request):  # Corrected function name
#     if request.method == 'POST':
#         obc = StudentInfo()
#         obc.name = request.POST.get('name')
#         obc.age = request.POST.get('age')
#         obc.gender = request.POST.get('gender')
#         obc.experience = request.POST.get('experience')
#         obc.address = request.POST.get('address')
#         obc.phone = request.POST.get('phone')
#         obc.email = request.POST.get('email')
#
#         # Save the data
#         obc.save()
#         return HttpResponse("Registration successful.")
#     return render(request, 'student/registration.html')


def logview(request):  # Corrected function name and indentation
    if request.method == 'POST':
        obd = LoginInfo()
        obd.user_name = request.POST.get('username')
        obd.password = request.POST.get('password')

        # Save the data
        obd.save()
        return HttpResponse("Login information saved successfully.")
    return HttpResponse("Method not allowed.", status=405)



def student_mainpage(request):
    return render(request, 'student/studentmain.html')