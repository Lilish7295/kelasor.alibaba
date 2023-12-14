from django.http.response import HttpResponse,JsonResponse

def list2(request):
    bus={
            "name":"scania",
            "trip_number":"7653",
            "seats_number":"44",
            "price":"270000"
            }
    return JsonResponse(bus)
