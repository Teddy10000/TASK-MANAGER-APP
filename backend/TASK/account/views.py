from django.shortcuts import render
from django.http import JsonResponse

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

#importing the api decorator that converts function based view to api subclassclass views
from rest_framework.decorators import api_view


# Now using the restframework response rather than the json response
from rest_framework.response import Response


# CUSTOMIZIING THE TOKEN IN VIEWS TO RETURN THE NAME OF THE USER
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        # 

        return token

#USING THE SERIALIZER ON THE TOKEN TO MAKE IT JSON READABLE    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer  

    
# Just the getRoue Function defining the paths for the url and returns as ajson response 
# the code defines a Django view function that handles a GET request, it creates a list of routes, and returns that list as a response in the body of the response with a status code of 200(OK)
@api_view(['GET'])
def getRoute(request):
    
    routes = [
        'api/token',
        'api/token/refresh',
    ]    
    return Response(routes) 