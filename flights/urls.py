from .views import list,list1
from django.urls import path, include
urlpatterns = [
    path('list', list , name='list'),
    path('list1', list1 , name='list1')
]