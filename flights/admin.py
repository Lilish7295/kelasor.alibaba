from django.contrib.admin import ModelAdmin, register
from .models import Flight,Airport

@register(Flight)
@register(Airport)

class Flightadmin(ModelAdmin):
    pass


class AirportAdmin(ModelAdmin):
    pass

