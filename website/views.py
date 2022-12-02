from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def about(request):
    return render(request, 'about.html',{})

def about1(request):
    return render(request, 'about1.html', {})

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