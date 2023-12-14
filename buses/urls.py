from .views import list2
from django.urls import path, include
urlpatterns = [
    path('list2', list2 , name='list2')
]
