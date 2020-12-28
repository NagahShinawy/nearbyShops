from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop

# admin.site.register(Shop)


@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'city', 'address', 'location')
    list_per_page = 20
    search_fields = ('name', 'location')
