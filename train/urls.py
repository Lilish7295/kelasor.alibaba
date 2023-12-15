from .views import list,list2
from django.urls import path, include
urlpatterns = [
    path('list', list , name='list')
]
urlpatterns = [
    path('list1', list2 , name='list1')
]