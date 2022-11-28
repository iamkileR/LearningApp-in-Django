from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('about1', views.about1, name='about1'),
    path('quiz', views.quiz, name='quiz'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('', include("django.contrib.auth.urls")),
]
