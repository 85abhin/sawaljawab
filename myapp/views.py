from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def base(request):
    return render(request,'myapp/base.html')

def home(request):
    return render(request,'myapp/home.html')

# ---------------------------------------------------------------------
def currentaffairs(request):
    return render(request,'myapp/currentaffairs.html')


# In reasoning page, all reasoning topics list here..
def reasoning(request):
    return render(request,'myapp/reasoning.html')

def reasoning_questions(request,category_slug):
    maths_and_reasoning=Maths_and_Reasoning.objects.filter(question_topic=category_slug) 
    paginator = Paginator(maths_and_reasoning, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'myapp/sawaljawab.html',{'page_obj':page_obj})

# ----------------------------- aptitude questions here ------------------------------------
def aptitude(request):
    return render(request,'myapp/aptitude.html')

# ----------------------------- English questions here ------------------------------------
def english(request):
    return render(request,'myapp/english.html')

def english_questions(request,category_slug):
    english=English_and_literature.objects.filter(question_topic=category_slug) 
    paginator = Paginator(english, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'myapp/sawaljawab.html',{'page_obj':page_obj})


# ----------------------------- ગુજરાતી questions here ------------------------------------
def gujarati(request):
    return render(request,'myapp/gujarati.html')


def gujarati_questions(request,category_slug):
    gujarati=Gujarati_and_literature.objects.filter(question_topic=category_slug) 
    paginator = Paginator(gujarati, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'myapp/sawaljawab.html',{'page_obj':page_obj})


# ----------------------------- Computer Operator questions here ------------------------------------
# def computer(request):
#     return render(request,'myapp/gujarati.html')


def computer_questions(request,category_slug):
    comp=Computer_Operator.objects.filter(question_topic=category_slug) 
    paginator = Paginator(comp, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'myapp/sawaljawab.html',{'page_obj':page_obj})

# --------------general Knowledge--------------------------------------

def GK(request):
    return render(request,'myapp/gk.html')


def GK_questions(request,category_slug):
    gk=General_knowledge.objects.filter(question_topic=category_slug) 
    paginator = Paginator(gk, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'myapp/sawaljawab.html',{'page_obj':page_obj})


# ---------------CurrentAfairs Questions -------
# def computer(request):
#     return render(request,'myapp/gujarati.html')


def currentAffairs_questions(request,category_slug):
    current=Current_Affairs2.objects.filter(question_topic=category_slug) 
    paginator = Paginator(current, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'myapp/sawaljawab.html',{'page_obj':page_obj})



# All old exam question papers here...
def Old_Question_Paper(request):
    return render(request,'myapp/oldquestion.html')


def Old_questions(request,category_slug):
    Old_que=Question_Paper.objects.filter(question_topic=category_slug) 
    paginator = Paginator(Old_que, 4) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'myapp/sawaljawab.html',{'page_obj':page_obj})

















# ----------------------------- About Us here ------------------------------------
def AboutUs(request):
    return render(request,'myapp/aboutus.html')


