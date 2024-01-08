from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
        path('base/',views.base),
        path('home/',views.home,name='homepage'),
        path('currentaffairs/',views.currentaffairs,name='currentaffairspage'),
        path('sawaljawab/',views.sawaljawab,name='sawaljawabpage'),
]
