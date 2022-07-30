from django.contrib import admin
from .models import Driver

# Register your models here.
# admin.site.register(Realtor)

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
      list_display=('id','name','email','hire_date')
      list_per_page=('id','name')
      search_fields=('name',)
      list_per_page=20