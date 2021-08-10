from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail,BadHeaderError
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from users.models import Disease
import requests
from random import choice,sample
from .models import Bookmark

API_KEY='00926f1959524f2996e2c35b16eb80f3'

# Create your views here.

def home(request):
    url=f'http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={API_KEY}'
    response=requests.get(url=url)
    data=response.json()
    articles=data['articles']
    if Disease.objects.filter(user=request.user.id):
        url2=f'https://api.fda.gov/drug/label.json?search=indications_and_usage:{choice(Disease.objects.filter(user=request.user.id))}&limit=20'
        response2=requests.get(url2)
        data2=response2.json()
        if 'results' in data2:
            middle=data2['results']
            list_med=[]
            for result in middle:
                if 'generic_name' in result['openfda']:
                    list_med.append(result)
            context={
                'articles':sample(articles,4),
                'diseases':sample(list_med,4)
            }
    else:
        common_disease=['fever','allergies','colds','diarrhea','headaches','stomach aches']
        url3=f'https://api.fda.gov/drug/label.json?search=indications_and_usage:{choice(common_disease)}&limit=20'
        response3=requests.get(url3)
        data3=response3.json()
        middle=data3['results']
        list_med=[]
        for result in middle:
            if 'generic_name' in result['openfda']:
                list_med.append(result)
        context={
            'articles':sample(articles,4),
            'diseases':sample(list_med,4)
        }
    return render(request,"homepage/homepage.html",context)

def news_all(request):
    url=f'http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={API_KEY}'
    response=requests.get(url=url)
    data=response.json()
    articles=data['articles']
    context={
        'articles':articles,
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
        url=f'https://api.fda.gov/drug/label.json?search={searched}&limit=40'
        response=requests.get(url=url)
        data=response.json()
        if 'results' in data:
            medicines=data['results']
            context={
                'medicines':medicines,
                'searched':searched
            }
        else:
            medicines=data['error']
            context={
                'medicines':medicines,
                'searched':searched
            }
        return render(request,'homepage/search_medicine.html',context)
    else:
        return render(request,'homepage/search_medicine.html',{})

def read_more(request,id):
    url=f'https://api.fda.gov/drug/label.json?search=openfda.spl_id:{id}&limit=20'
    response=requests.get(url=url)
    data=response.json()
    medicines=data['results']
    for result in medicines:
        if result['openfda']['spl_id'][0] == id:
            context={
                'medicine':result
            }
    if request.user:
        if Bookmark.objects.filter(user=request.user.id,spl_id=context['medicine']['openfda']['spl_id'][0]):
            return render(request,'homepage/med_bookmark_remove.html',context)
        else:
            return render(request,'homepage/med_read_more.html',context)
    else:
        return render(request,'homepage/med_read_more.html',context)

@login_required
def bookmark(request,id):
    if Bookmark.objects.filter(spl_id=id):
        return redirect('new_read_more',id)
    else:
        Bookmark.objects.create(user=request.user, spl_id=id)
        messages.success(request,f"Medicine is Bookmarked")
        return redirect('new_read_more',id)

@login_required
def remove_bookmark(request,id):
    Bookmark.objects.filter(spl_id=id).delete()
    return redirect('med_read_more',id)

@login_required
def new_read_more(request,id):
    url=f'https://api.fda.gov/drug/label.json?search=openfda.spl_id:{id}&limit=20'
    response=requests.get(url=url)
    data=response.json()
    medicines=data['results']
    for result in medicines:
        if result['openfda']['spl_id'][0] == id:
            context={
                'medicine':result
            }
    return render(request,'homepage/med_bookmark_remove.html',context)

    