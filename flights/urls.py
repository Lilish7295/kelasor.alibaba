from .views import list
from django.urls import path, include
urlpatterns = [
    path('list', list , name='list')
]
