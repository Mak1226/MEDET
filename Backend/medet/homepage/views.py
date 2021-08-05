from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail,BadHeaderError
from django.db.models import Q
import requests
API_KEY='00926f1959524f2996e2c35b16eb80f3'

# Create your views here.

def home(request):
    url=f'http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={API_KEY}'
    response=requests.get(url=url)
    data=response.json()
    articles=data['articles']
    context={
        'articles':articles[0:1],
        'articles1':articles[1:2]
        
    }
    return render(request,"homepage/homepage.html",context)

def news_all(request):
    url=f'http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={API_KEY}'
    response=requests.get(url=url)
    data=response.json()
    articles=data['articles']
    context={
        'articles':articles
    }
    return render(request,"homepage/news_all.html",context)

def about(request):
    return render(request,"homepage/about.html")


def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            subject="website inquiry"
            body={
                'full_name':form.cleaned_data['full_name'],
                'email':form.cleaned_data['email'],
                'message':form.cleaned_data['message']
            }
            message="\n".join(body.values())

            try:
                send_mail(subject,message,body['email'],['MEDET.mail124@gmail.com'])
                messages.success(request,f"Your message has been delivered!!")
            except BadHeaderError:
                return HttpResponse('INVALID HEADER FOUND')
            return redirect('contact')
    form=ContactForm()
    return render(request,"homepage/contact.html",{'form':form})

def search_med(request):
    
    if request.method=='POST':
        searched=request.POST['home_input']
        url=f'https://api.fda.gov/drug/label.json?search={searched}&limit=20'
        response=requests.get(url=url)
        data=response.json()
        if 'results' in data:
            medicines=data['results']
            context={
                'medicines':medicines
            }
        else:
            medicines=data['error']
            context={
                'medicines':medicines
            }
        return render(request,'homepage/search_medicine.html',context)
    else:
        return render(request,'homepage/search_medicine.html',{})

def read_more(request,id):
    print(id)
    url=f'https://api.fda.gov/drug/label.json?search={id}'
    response=requests.get(url=url)
    data=response.json()
    medicines=data['results']
    context={
        'medicines':medicines
    }
    return render(request,'homepage/med_read_more.html',context)