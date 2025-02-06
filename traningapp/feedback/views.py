from django.shortcuts import render
from django.http import HttpResponse
from feedback.models import Feedback

# Create your views here.
def feedback(request):
    if request.method == 'POST':
        obj=Feedback()
        obj.st_name =request.POST.get('stdname')
        obj.feedback =request.POST.get('feedback')
        obj.save()


    return render(request, 'feedback/adfeedback.html')

def viewfeedback(request):
    obj=Feedback.objects.all()
    context={
        'fb':obj
    }
    return render(request,'feedback/viewfeedback.html',context)