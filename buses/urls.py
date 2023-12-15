from .views import list,list2
from django.urls import path, include
urlpatterns = [
    path('list', list , name='list'),
    path('list2', list2 , name='list2')
]

