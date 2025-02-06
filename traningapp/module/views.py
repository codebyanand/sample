from django.shortcuts import render
from module.models import  Module
from django.http import HttpResponse

# Create your views here.
def module(request):
    if request.method =='POST':
        object=Module()
        object.course_name =request.POST.get('course')
        object.module_name =request.POST.get('module')
        object.save()

    return render(request,'module/add module.html')
def viewmodule(request):
    obj=Module.objects.all()
    context={
        'mod':obj
    }
    return render(request,'module/viewmodule.html',context)