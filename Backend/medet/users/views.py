from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import UserRegistrationForm, UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required 
from .models import Medicine,Disease,Doctor,Reports
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
from django import forms
from homepage.models import Bookmark
import requests

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
    context={
        'medicines':Medicine.objects.filter(user=request.user.id)[:4][::-1],
        'diseases':Disease.objects.filter(user=request.user.id)[:4][::-1],
        'schedules':Medicine.objects.filter(user=request.user.id)[:4][::-1],
        'doctors':Doctor.objects.filter(user=request.user.id)[:4][::-1]
    }
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
    

@login_required
def medicine(request):
    context={'medicines':Medicine.objects.filter(user=request.user.id)[::-1]}
    return render(request,'users/medcines.html',context)
@login_required
def doctor(request):
    context={'doctors':Doctor.objects.filter(user=request.user.id)[::-1]}
    return render(request,'users/doctors.html',context)
@login_required
def schedule(request):
    context={'schedules':Medicine.objects.filter(user=request.user.id)[::-1]}
    return render(request,'users/schedules.html',context)
@login_required
def disease(request):
    context={'diseases':Disease.objects.filter(user=request.user.id)[::-1]}
    return render(request,'users/diseases.html',context)

def med_report(request):
    context={'reports':Reports.objects.filter(user=request.user.id)[::-1]}
    return render(request,'users/reports.html',context)

class MedicalForm(forms.ModelForm):
    class Meta:
       model = Medicine
       fields=['medicine_name','disease_name','schedule','doctor_name','image']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(MedicalForm, self).__init__(*args, **kwargs)
       self.fields['doctor_name'].queryset = Doctor.objects.filter(user=user)
       self.fields['disease_name'].queryset = Disease.objects.filter(user=user)



class MedicineDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model=Medicine

    def test_func(self):
        medicine=self.get_object()
        if self.request.user == medicine.user:
            return True
        return False

class MedicineCreateView(LoginRequiredMixin,CreateView):
    model=Medicine
    form_class = MedicalForm

    def get_form_kwargs(self):
        kwargs = super(MedicineCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



    def form_valid(self,form):
        
        form.instance.user=self.request.user
        return super().form_valid(form)

class MedicineUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Medicine
    form_class = MedicalForm

    def get_form_kwargs(self):
        kwargs = super(MedicineUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    def test_func(self):
        medicine=self.get_object()
        if self.request.user == medicine.user:
            return True
        return False

class MedicineDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Medicine
    success_url='/profile/medicine/'

    def test_func(self):
        medicine=self.get_object()
        if self.request.user == medicine.user:
            return True
        return False


class DoctorDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model=Doctor

    def test_func(self):
        doctor=self.get_object()
        if self.request.user == doctor.user:
            return True
        return False

class DoctorUpdateView(LoginRequiredMixin,UpdateView):
    model=Doctor
    fields=['doctor_name','address','contact']

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class DoctorCreateView(LoginRequiredMixin,CreateView):
    model=Doctor
    fields=['doctor_name','address','contact']

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)



class DoctorDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Doctor
    success_url='/profile/doctor/'

    def test_func(self):
        medicine=self.get_object()
        if self.request.user == medicine.user:
            return True
        return False



class DiseaseDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model=Disease

    def test_func(self):
        disease=self.get_object()
        if self.request.user == disease.user:
            return True
        return False

class DiseaseUpdateView(LoginRequiredMixin,UpdateView):
    model=Disease
    fields=['disease_name','disease_type','onset_of_disease','symptoms','affected_area']

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class DiseaseCreateView(LoginRequiredMixin,CreateView):
    model=Disease
    fields=['disease_name','disease_type','onset_of_disease','symptoms','affected_area']

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)



class DiseaseDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Disease
    success_url='/profile/disease/'

    def test_func(self):
        medicine=self.get_object()
        if self.request.user == medicine.user:
            return True
        return False



class ReportsDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model=Reports

    def test_func(self):
        reports=self.get_object()
        if self.request.user == reports.user:
            return True
        return False

class ReportsUpdateView(LoginRequiredMixin,UpdateView):
    model=Reports
    fields=['title','description','medical_report']

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class ReportsCreateView(LoginRequiredMixin,CreateView):
    model=Reports
    fields=['title','description','medical_report']

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)



class ReportsDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Reports
    success_url='/profile/reports/'

    def test_func(self):
        reports=self.get_object()
        if self.request.user == reports.user:
            return True
        return False


@login_required
def bookmark_list(request):
    bookmarks=Bookmark.objects.filter(user=request.user.id)
    list_bookmark=[]
    for bookmark in bookmarks:
        url=f'https://api.fda.gov/drug/label.json?search=openfda.spl_id:{bookmark.spl_id}&limit=20'
        response=requests.get(url=url)
        data=response.json()
        medicines=data['results']
        for result in medicines:
            if result['openfda']['spl_id'][0] == bookmark.spl_id:
                list_bookmark.append(result)
    return render(request,'users/bookmarks_list.html',{'bookmarks':list_bookmark})