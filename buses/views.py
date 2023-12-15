from django.http.response import HttpResponse,JsonResponse
from.models import Terminal, Bus

def list(request):
    terminals=Terminal.objects.all()
    terminals_list=[]
    for item in terminals:
        dictionary={
            "name" : item.name,
            "no" : item.no,
            "city" : item.city
        }
    terminals_list.append(dictionary)
    return JsonResponse(terminals_list,safe=False)

def list2(request):
    buses=Bus.objects.all()
    buses_list=[]
    for item in buses:
        dictionary={
            "origin" : item.origin.name,
            "destination" : item.destination,
            "name" : item.name
        }
    buses_list.append(dictionary)
    return JsonResponse(buses_list,safe=False)
