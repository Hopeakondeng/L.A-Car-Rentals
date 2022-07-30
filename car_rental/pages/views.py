from django.http import HttpResponse
from django.shortcuts import render
from drivers.models import Driver
from rentals.choices import seats_choices,city_choices,price_choices
from rentals.models import Rentals

# Create your views here.

def index(request):
    rentals=Rentals.objects.order_by('-list_date').filter(is_available=True)[:3]
    
    context ={
         'rentals':rentals,
         'city_choices':city_choices,
         'seats_choices': seats_choices,
         'price_choices': price_choices
    }
    return render(request, 'pages/home.html',context)
    
def about(request):
    # get all the realtore
    drivers = Driver.objects.order_by('-hire_date')
    # get MVP
    mvp_drivers =Driver.objects.all().filter(is_mvp=True)
    context = {
         'drivers':drivers,
         'mvp_drivers':mvp_drivers,
    }
    return render(request, 'pages/about.html',context)