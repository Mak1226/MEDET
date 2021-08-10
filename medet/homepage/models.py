from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Bookmark(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    spl_id=models.TextField(null=True)