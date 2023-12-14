from django.contrib.admin import ModelAdmin, register
from .models import Terminal,Bus

@register(Terminal)
class Terminaladmin(ModelAdmin):
    pass
@register(Bus)
class BusAdmin(ModelAdmin):
    list_display=['origin','destination']
    search_fields=['origin']
    list_filter=['origin']


