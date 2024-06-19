from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from .models import Livre
# Create your views here.


    
def home(request):
    livres = Livre.objects.all()
    return render(request, "library/home.html", {"livres": livres})

def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        user = forms.UserRegisterForm()
        return render(request, "library/register.html", {"form": user})
        

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return render(request, "library/home.html", {"user": user})
    else:
        form = AuthenticationForm()
    return render(request, 'library/login.html', {'form': form})
        