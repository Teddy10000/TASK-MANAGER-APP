from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


# Create your views here.


from rest_framework.decorators import authentication_classes, permission_classes


class NoteViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    def get_queryset(self):
        #return Notes.objects.filter(user_id=self.request.user)
        queryset = Notes.objects.all()
        user_id = self.request.query_params.get("user_id", None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset
   
   
    
    
    
    
    
