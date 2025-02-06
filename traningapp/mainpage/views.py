from django.shortcuts import render

# Create your views here.
def user(us):
    return render(us,'mainpage/mainpage.html')