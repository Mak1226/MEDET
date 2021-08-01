from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,"homepage/homepage.html")

def about(request):
    return render(request,"homepage/about.html")

def contact(request):
    return render(request,"homepage/contact.html")