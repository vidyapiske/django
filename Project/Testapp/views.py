from django.shortcuts import render
from django.http import HttpResponse

def Hii(request):
    return render(request,'App/index.html')
def Hello(request):
    return render(request,'App/about.html')


# Create your views here.
