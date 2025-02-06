from django.shortcuts import render
from teacher.models import TeachersReg
from student.models import StudentInfo, LoginInfo
from django.http import HttpResponse
def techerpage(request):
    if request.method == 'POST':
        obc = TeachersReg()
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
        ob.user_type="teacher"
        ob.save()
        return HttpResponse("Registration successful.")
    return render(request,'teacher/teachersreg.html')
def logview(request):  # Corrected function name and indentation
    if request.method == 'POST':
        obd = LoginInfo()
        obd.user_name = request.POST.get('username')
        obd.password = request.POST.get('password')

        # Save the data
        obd.save()
        return HttpResponse("Login information saved successfully.")
    return HttpResponse("Method not allowed.", status=405)



def teacher_mainpage(request):
    return render(request, 'teacher/teacherslogin.html')


def teacher_main(request):
    return render(request, 'teacher/main.html')

