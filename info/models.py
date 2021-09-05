from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Items(models.Model):
    
    userid=models.CharField(max_length=1000,default="101")
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=10)
    status = models.IntegerField()
    date = models.DateField(default="04-09-2021")


