from email.policy import default
from django.db import models
from drivers.models import Driver
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Rentals(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.DO_NOTHING)
    name= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    seats=models.IntegerField()
    mileage=models.IntegerField()
    photo_main=models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    photo_1=models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    photo_2=models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    photo_3=models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    photo_4=models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    photo_5=models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    photo_6=models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    is_available=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.name

class RentalDetails(models.Model):
    rent_date = models.DateTimeField(default=datetime.now, blank=True)
    return_date = models.DateTimeField(null=True)
    duration = models.IntegerField()
    name = models.ForeignKey(Rentals, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Review(models.Model):
    comment = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    car = models.ForeignKey(Rentals,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


    
    
