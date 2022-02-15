from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def contact(request):
    return render(request, 'contact.html')


def mySystem(request):
    return render(request, 'my-system.html')


def singleCourse(request):
    return render(request, 'single-course.html')


def user(request):
    return render(request, 'user.html')

