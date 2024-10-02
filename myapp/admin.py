from django.contrib import admin

# Register your models here.

from .models import Countries 

@admin.register(Countries)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name','capital']
    list_per_page = 3 # django admin page pagination 
    