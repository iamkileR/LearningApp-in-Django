from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('rozwijana_1', views.rozwijana_1, name='rozwijana_1'),
    path('rozwijana_2', views.rozwijana_2, name='rozwijana_2'),
    path('menu_aproksymacja', views.menu_aproksymacja, name='menu_aproksymacja'),
    path('menu_interpolacja', views.menu_interpolacja, name='menu_interpolacja'),
    path('menu_rozniczkowanie', views.menu_rozniczkowanie, name='menu_rozniczkowanie'),
    path('menu_calkowanie', views.menu_calkowanie, name='menu_calkowanie'),
    path('quiz', views.quiz, name='quiz'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('', include("django.contrib.auth.urls")),
]

urlpatterns += staticfiles_urlpatterns()