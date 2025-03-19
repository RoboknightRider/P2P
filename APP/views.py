from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'Home.html')

def register(request):
    return render(request, 'Register.html')

def login(request):
    return render(request, 'Login.html')