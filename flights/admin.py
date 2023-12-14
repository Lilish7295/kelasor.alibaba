from django.contrib.admin import ModelAdmin, register
from .models import Flight,Airport



@register(Flight)
class Flightadmin(ModelAdmin):
    autocomplete_fields = ['origin']

@register(Airport)
class AirportAdmin(ModelAdmin):
    list_display=["name", "no", "adress"]
    search_fields=['name']
    list_filter=['city']

