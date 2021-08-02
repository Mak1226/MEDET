from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required 


# Create your views here.

def register(request):
    if request.method =='POST':
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data.get('first_name')
            username=form.cleaned_data.get('username')
            if name:
                messages.success(request,f"Account Created for {name}! Login now!")
            else:
                messages.success(request,f"Account Created for {username}! Login now!")
            return redirect('login')

    else:
        form= UserRegistrationForm()

    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')