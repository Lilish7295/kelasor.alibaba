from django.http.response import HttpResponse,JsonResponse

def wellcome(request):
    return HttpResponse("wellcome to this page")

def about(request):
    return HttpResponse("here is about this page!")

def contact(request):
    return HttpResponse("here is contact")

