from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def register(request):
    return HttpResponse('register')

def login(request):
    return render(request, 'base/login.html')

def dashbord(request):
    return HttpResponse('dashbord')

