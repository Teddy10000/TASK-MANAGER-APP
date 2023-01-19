from django.shortcuts import render
from django.http import JsonResponse

#importing the api decorator that converts function based view to api subclassclass views
from rest_framework.decorators import api_view


# Now using the restframework response rather than the json response
from rest_framework.response import Response


# Create your views here.



    
# Just the getRoue Function defining the paths for the url and returns as ajson response 

@api_view(['GET'])
def getRoute(request):
    
    routes = [
        'api/token',
        'api/token/refresh',
    ]    
    return Response(routes) 