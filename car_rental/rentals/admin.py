from django.contrib import admin
from .models import RentalDetails, Rentals
# Register your models here.

@admin.register(Rentals)
class RentalsAdmin(admin.ModelAdmin):
    list_display=('id','name','is_available','price','list_date','driver')
    list_display_links= ('id','name')
    list_filter= ('driver',)
    list_editable=('is_available',)
    search_fields= ('name','description','city','state','price')
    list_per_page=20

@admin.register(RentalDetails)
class RentalDetailsAdmin(admin.ModelAdmin):
    list_display=('rent_date','return_date','duration','name','user')
    list_display_links= ('user','name')
    list_filter= (['rent_date'])
    list_editable=(['return_date'])
    search_fields= ('name','rent_date','return_date','name','user')
    list_per_page=20
    
# admin.site.register(Rentals) 