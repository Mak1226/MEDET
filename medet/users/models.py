from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    age=models.PositiveIntegerField(null=True)
    date_of_birth=models.DateField(null=True)
    blood_type=models.CharField(max_length=3,null=True,blank=True)
    weight=models.PositiveIntegerField(null=True,blank=True)
    height=models.PositiveIntegerField(null=True,blank=True)
    allergy=models.TextField(blank=True,null=True)
    contact=models.CharField(max_length=10,null=True)
    address=models.TextField(null=True)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    doctor_name=models.CharField(max_length=100, null=True)
    address=models.TextField(null=True,blank=True)
    contact=models.CharField(max_length=10,null=True,blank=True)

    def get_absolute_url(self):
        return reverse('profile_doctor')

    def __str__(self):
        return self.doctor_name

class Disease(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    disease_type=models.CharField(max_length=500,null=True,blank=True)
    disease_name=models.CharField(max_length=200,null=True)
    affected_area=models.TextField(null=True,blank=True)
    onset_of_disease=models.CharField(max_length=200,null=True,blank=True)
    symptoms=models.TextField(null=True,blank=True)

    def get_absolute_url(self):
        return reverse('profile_disease')

    def __str__(self):
        return self.disease_name

class Medicine(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    medicine_name=models.CharField(max_length=200,null=True)
    doctor_name=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)
    disease_name=models.ForeignKey(Disease,on_delete=models.CASCADE,null=True,blank=True)
    schedule=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='medicine_pics',blank=True)


    def get_absolute_url(self):
        return reverse('profile_medicine')

class Reports(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,null=True,blank=True)
    medical_report=models.ImageField(upload_to='med_report',null=True)
    description=models.TextField(null=True,blank=True)

    def get_absolute_url(self):
        return reverse('profile_med_reports')

    def __str__(self):
        return self.title


