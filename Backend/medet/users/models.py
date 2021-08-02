from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    age=models.PositiveIntegerField(null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    blood_type=models.CharField(max_length=3,null=True,blank=True)
    weight=models.PositiveIntegerField(null=True,blank=True)
    height=models.PositiveIntegerField(null=True,blank=True)
    allergy=models.TextField(blank=True,null=True)
    contact=models.CharField(max_length=10,null=True)
    address=models.TextField(null=True)

    def __str__(self):
        return self.user.username

class Medicine(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    medicine_name=models.TextField(null=True)

