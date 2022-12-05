from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def rozwijana_1(request):
    return render(request, 'rozwijana_1.html',{})

def rozwijana_2(request):
    return render(request, 'rozwijana_2.html',{})

def menu_aproksymacja(request):
    return render(request, 'menu_aproksymacja.html',{})

def menu_interpolacja(request):
    return render(request, 'menu_interpolacja.html', {})

def menu_rozniczkowanie(request):
    return render(request, 'menu_rozniczkowanie.html', {})

def menu_calkowanie(request):
    return render(request, 'menu_calkowanie.html', {})

def quiz(request):
    return render(request, 'quiz.html', {})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {"form":form})

def login(request):
    return render(request, 'registration/login.html', {})