from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
        path('base/',views.base),
        path('',views.home,name='homepage'),
        path('currentaffairs/',views.currentaffairs,name='currentaffairspage'),
        # path('sawaljawab/',views.sawaljawab,name='sawaljawabpage'),
        path('reasoning/',views.reasoning,name='reasoningpage'),
        path('reasoning_questions/<slug:category_slug>/',views.reasoning_questions,name='reasoningquestionspage'),
        path('aptitude/',views.aptitude,name='aptitudepage'),
        path('english/',views.english,name='englishpage'),
        path('english_questions/<slug:category_slug>/',views.english_questions,name='englishquestionspage'),
        path('gujarati/',views.gujarati,name='gujaratipage'),
        path('gujarati_questions/<slug:category_slug>/',views.gujarati_questions,name='gujaratiquestionspage'),
        path('computer_operator/<slug:category_slug>/',views.computer_questions,name='computer_questions'),
        path('current_affairs/<slug:category_slug>/',views.currentAffairs_questions,name='currentaffairs_questions'),
        path('generalknowledge/',views.GK,name='general_knowledge'),
        path('generalknowledge/<slug:category_slug>/',views.GK_questions,name='gk_questions'),
        path('aboutus/',views.AboutUs,name='aboutus'),
]
