from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class Meta:
        model =User
        fields=['username','first_name','last_name','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField(required=True)
    class Meta:
        model =User
        fields=['username','first_name','last_name','email']

class ProfileUpdateForm(forms.ModelForm):
    age=forms.IntegerField()
    date_of_birth=forms.DateField(localize=True,widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type':'date'}))
    contact=forms.CharField(max_length=10,)
    address=forms.CharField(required=False)
    blood_type=forms.CharField(max_length=3,required=False)
    allergy=forms.CharField(max_length=500,required=False)
    weight=forms.IntegerField(required=False)
    height=forms.IntegerField(required=False)

    class Meta:
        model=Profile
        fields=['image','age','date_of_birth','contact','address','blood_type','allergy','weight','height']