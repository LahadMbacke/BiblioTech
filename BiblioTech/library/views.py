from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

# def home(request):
#     return render(request, "library/home.html")

def register(request):
    form = forms.UserRegisterForm()
    return render(request, "library/register.html" ,{"form": form})

def login(request):
    form = forms.UserRegisterForm()
    return render(request, "library/login.html", {"form": form})