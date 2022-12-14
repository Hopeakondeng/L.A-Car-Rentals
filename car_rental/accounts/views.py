from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User#module de django
from django.contrib import auth
from rentals.models import RentalDetails
from contacts.models import Contact
# Create your views here.
def register(request):
    if request.method == "POST":
        # get form values
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']
        
        # check if password match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # looks good
                    user= User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.save()
                    messages.success(request,'you are now registered and can log in')
                    return redirect('login')
    else:            
        return render(request, 'accounts/register.html')
    
def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'you are now logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'INVALID CREDENTIALS, try again...')
            return redirect('login')
    
    
    return render(request, 'accounts/login.html')
    
def dashboard(request):
    user_contacts = RentalDetails.objects.order_by('-rent_date').filter(user_id=request.user.id)
    
    context = {
       'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html',context)
    
def logout(request):
    auth.logout(request)
    messages.success(request, 'you are LOGGED OUT')
    return redirect('index')