from django.http.response import HttpResponse,JsonResponse
from.models import Station, Train


def list(request):
    stations=Station.objects.all()
    stations_list=[]
    for item in stations:
        dictionary={
            "name" : item.name,
            "no" : item.no.name,
            "city" : item.city
        }
    stations_list.append(dictionary)
    return JsonResponse(stations_list,safe=False)

def list2(request):
    trains=Train.objects.all()
    trains_list=[]
    for item in trains:
        dictionary={
            "origin" : item.origin.name,
            "destination" : item.destination,
            "name" : item.name
        }
    trains_list.append(dictionary)
    return JsonResponse(trains_list,safe=False)