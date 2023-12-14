from django.http.response import HttpResponse,JsonResponse

def list(request):
    flight={
            "name":"boeing707",
            "flight_number":"7653",
            "seats_number":"266",
            "price":"1200000"
            }
    return JsonResponse(flight)