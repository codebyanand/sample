from django.shortcuts import render
from doubts.models import Doubt
from django.http import HttpResponse

# Create your views here.
def doubt(request):
    if request.method == 'POST':
        obj =Doubt()
        obj.doubts = request.POST.get('dut')
        obj.response = 'pending'
        obj.student_name = request.POST.get('std')
        obj.save()
    return render(request,'doubts/add doubts.html')

def respons(res):
    return render(res,'doubts/add respons.html')
