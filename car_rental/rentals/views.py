from unicodedata import name
from django.shortcuts import redirect, render,get_object_or_404
from django.core.paginator import Paginator

from .forms import AddReviewForm
from .models import RentalDetails, Rentals, Review
from rentals.choices import seats_choices,city_choices,price_choices


# Create your views here.
def rentals(request):
    rentals=Rentals.objects.order_by('-list_date').filter(is_available=True)#-list_date ordre desc
    paginator=Paginator(rentals,3)
    page= request.GET.get('page')#page recupere et mets ces donnees
    paged_rentals=paginator.get_page(page)
    context={
        'rentals':paged_rentals
    }
    return render(request,'rentals/rentals.html',context)
    
def rental(request,rental_id):
    rental= get_object_or_404(Rentals,pk=rental_id)
    review = Review.objects.filter(car= rental)
    form = AddReviewForm()
    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(comment=form.cleaned_data['comment'], car = rental, user = request.user)
            return redirect('rental', rental_id)
        else:
            pass

    rental_details = RentalDetails.objects.filter(name=rental, return_date=None).first()
    print(rental_details)

    context = {
    'rental':rental,
    'review':review,
    'form':form,
    }
    return render(request,'rentals/rental.html',context)

def search(request):
    queryset_list = Rentals.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(name__icontains=keywords)

     # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

     # Seats
    if 'seats' in request.GET:
        seats = request.GET['seats']
        if seats:
            queryset_list = queryset_list.filter(seats__lte=seats)

   # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
     'city_choices': city_choices,
     'seats_choices': seats_choices,
     'price_choices': price_choices,
     'rentals': queryset_list,
     'values': request.GET
   }

    return render(request, 'rentals/search.html',context)