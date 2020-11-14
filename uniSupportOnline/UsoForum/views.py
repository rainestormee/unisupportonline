from django.shortcuts import render
from django.http import HttpResponse
import sys, os

# Create your views here.

def home(request):
    return HttpResponse('<h1>Home Page</h1>')
def forum(request):
    return HttpResponse('<h1>Forum Page</h1>')
def about(request):
    return render(request,'about.html')
