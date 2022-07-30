from django.urls import path
from . import views
urlpatterns = [
    path('', views.rentals, name='rentals' ),
    path('<int:rental_id>/rental', views.rental, name='rental' ),
    path('search', views.search, name='search' ),
    
]