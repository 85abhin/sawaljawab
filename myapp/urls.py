from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
        path('base/',views.base),
        path('home/',views.home,name='homepage'),
        path('currentaffairs/',views.currentaffairs,name='currentaffairspage'),
        # path('sawaljawab/',views.sawaljawab,name='sawaljawabpage'),
        path('reasoning/',views.reasoning,name='reasoningpage'),
        path('reasoning_questions/<slug:category_slug>/',views.reasoning_questions,name='reasoningquestionspage'),
        path('aptitude/',views.aptitude,name='aptitudepage'),
        path('english/',views.english,name='englishpage'),
        path('english_questions/<slug:category_slug>/',views.english_questions,name='englishquestionspage'),
        path('gujarati/',views.gujarati,name='gujaratipage'),
        path('aboutus/',views.AboutUs,name='aboutus'),
]
