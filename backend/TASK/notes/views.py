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
       return Notes.objects.all()
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)