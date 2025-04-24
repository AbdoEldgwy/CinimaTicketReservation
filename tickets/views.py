from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Movie, Reservation

# without REST framework
def no_rest_no_model(request):
    geusts = [
        {
            "id": 1,
            "name": "John",
            "phone": "1234567890"
        },
        {
            "id": 2,
            "name": "Mary",
            "phone": "9876543210"
        }
    ]
    return JsonResponse(geusts, safe=False)

# without REST framework with defualt response
def no_rest_with_model(request):
    data = Guest.objects.all() # get all guests from the database
    response = {
        "guests" : list(data.values("Name")) # convert the queryset to a list of dictionaries
    } 
    return JsonResponse(response)

# with REST framework