from django.shortcuts import render
from django.http import HttpResponse
import sys, os

# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def dashboard(request):
    return render(request,'dashboard.html')
def help(request):
    return render(request,'help.html')
def login(request):
    return render(request,'login.html')
def search(request):
    return render(request,'search.html')
def signup(request):
    return render(request,'signup.html')
def terms(request):
    return render(request,'terms.html')

