from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required 
from .models import Medicine,Profile
from django.views.generic import ListView


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
    context={'medicines':Medicine.objects.filter(user=self.request.user)}
    return render(request,'users/profile.html',context)

@login_required
def profile_update(request):
    if request.method =='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,"Your account has been updated!!")
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={'u_form':u_form,'p_form':p_form}
    return render(request,'users/profile_update.html',context)