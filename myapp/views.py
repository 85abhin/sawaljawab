from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'myapp/base.html')


def home(request):
    return render(request,'myapp/home.html')

# ---------------------------------------------------------------------
def currentaffairs(request):
    return render(request,'myapp/currentaffairs.html')

# This is question page where every question should be display here..
def sawaljawab(request):
    return render(request,'myapp/sawaljawab.html')

# In reasoning page, all resoning topics list here..
def reasoning(request):
    return render(request,'myapp/reasoning.html')

# ----------------------------- aptitude questions here ------------------------------------
def aptitude(request):
    return render(request,'myapp/aptitude.html')

# ----------------------------- English questions here ------------------------------------
def english(request):
    return render(request,'myapp/english.html')

# ----------------------------- ગુજરાતી questions here ------------------------------------
def gujarati(request):
    return render(request,'myapp/gujarati.html')

# ----------------------------- ગુજરાતી questions here ------------------------------------
def gujarati(request):
    return render(request,'myapp/gujarati.html')

# ----------------------------- About Us here ------------------------------------
def AboutUs(request):
    return render(request,'myapp/aboutus.html')


