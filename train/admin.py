from django.contrib.admin import ModelAdmin, register
from .models import Station,Train

@register(Station)
class Stationadmin(ModelAdmin):
    pass

@register(Train)
class Trainadmin(ModelAdmin):
    pass
