from django.http import HttpResponseRedirect

from login.models import LoginInfo
from django.shortcuts import render

def login(request):
    if request.method=='POST':
        p=request.POST.get('password')
        u=request.POST.get('username')

        obj=LoginInfo.objects.get(user_name=u, password=p)
        if obj.user_type=='teacher':

            return HttpResponseRedirect('/techmain/')
        elif obj.user_type=='student':
            return HttpResponseRedirect('/st_main/')
    return render(request,'login/login.html')