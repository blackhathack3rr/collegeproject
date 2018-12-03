from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.





class Business(models.Model):
    buser=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    pas=models.CharField(max_length=10)

    def __str__(self):
        return "{} in ({})".format(self.buser, self.email, self.phone,self.pas)

class Add(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    offers = models.CharField(max_length=50)
    hotelfacilities=models.CharField(max_length=1000)
    roomfacilities = models.CharField(max_length=1000)
    inhouseservice=models.CharField(max_length=1000)
    photo=models.ImageField()
    photo1=models.ImageField()


    def __str__(self):
        return "{} in ({})".format(self.name, self.location,self.price,self.offers,self.hotelfacilities,self.roomfacilities,self.inhouseservice,self.photo,self.photo1)