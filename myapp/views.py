from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'myapp/base.html')


def home(request):
    return render(request,'myapp/home.html')

def currentaffairs(request):
    return render(request,'myapp/currentaffairs.html')

def sawaljawab(request):
    return render(request,'myapp/sawaljawab.html')