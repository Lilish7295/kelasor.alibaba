from django.http.response import HttpResponse,JsonResponse
from.models import Flight, Airport


def list(request):
    flights=Flight.objects.all()
    flight_list=[]
    for item in flights:
        dictionary={
            "name" : item.name,
            "origin" : item.origin.name,
            "price" : item.price
        }
    flight_list.append(dictionary)
    return JsonResponse(flight_list,safe=False)

def list1(request):
    airports=Airport.objects.all()
    airport_list=[]
    for item in airports:
        dictionary= {
            "name" : item.name,
            "city" : item.city,
            "number" : item.no
        }
        airport_list.append(dictionary)
    return JsonResponse(airport_list,safe=False)