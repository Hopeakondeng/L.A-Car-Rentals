from dateutil.parser import parse
from django.conf import settings
from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from rentals.models import RentalDetails,Rentals
from datetime import *
# Create your views here.

def contact(request):
   
    if request.method == "POST":
        # get form values
        rental= request.POST['rental']
        rental_id= request.POST['rental_id']
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        message= request.POST['message']
        user_id= request.POST['user_id']
        driver_email= request.POST['driver_email']
        duration= request.POST['duration']
        rent_date= request.POST['rent_date']
        print(rent_date)
        

        car= Rentals.objects.filter(id=rental_id).first()
        print(car)
        '''stDate = rent_date.replace("\"", "")
        rent_date = datetime.strptime(stDate, "%Y-%m-%d")'''
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted= Contact.objects.all().filter(rental_id=rental_id, user_id=user_id)
            print(has_contacted)

            car_unavailable = RentalDetails.objects.filter(name=car, return_date=None).order_by('-rent_date').first()
            # print(car_unavailable.name)
            # print(car_unavailable.duration)
            # print(car_unavailable.rent_date )
            if car_unavailable :
                return_date =  car_unavailable.rent_date + timedelta(days=car_unavailable.duration)
                print(return_date)
                if parse(rent_date).timestamp() < parse(return_date.strftime("%Y-%m-%d")).timestamp():
                    messages.error(request,'This car is not available currently, it will only be available on the '+(return_date.strftime("%Y-%m-%d")) )
                    return redirect('rental', rental_id)
                elif parse(rent_date).timestamp() > parse(return_date.strftime("%Y-%m-%d")).timestamp() :
                    RentalDetails.objects.create(rent_date= rent_date, duration=duration, name = car, user_id= user_id)
                    messages.success(request, 'Your booking was successfully created, we will contact you shortly with more information. Thanks!')
                    return redirect('rental', rental_id)
            else:
                RentalDetails.objects.create(rent_date= rent_date, duration=duration, name = car, user_id= user_id)
                messages.success(request, 'Your booking was successfully created, we will contact you shortly with more information. Thanks!')
                # send email
                send_mail(
                    'Car Rental Inquiry',
                    'There has been an inquiry for' + rental +'. Contact me for more info',
                    settings.EMAIL_HOST_USER  ,
                    [driver_email, 'hopeakondeng@gmail.com'],
                    fail_silently=False
                )
                return redirect('rental', rental_id)
                

        
        
        
        contact = Contact(
             rental=rental,
            rental_id=rental_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )
        contact.save()
        
        messages.success(request, 'Your request has been submitted,a driver will get back to you soon')
            
        return redirect('/rentals/'+ rental_id+ '/rental') 