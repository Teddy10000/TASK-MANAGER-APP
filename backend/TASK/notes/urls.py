#from rest_framework import routers
from rest_framework_nested import routers
from .views import NoteViewset
from django.urls import path ,include





## CHANGED TO NESTED ROUTERS 
note_routes = routers.SimpleRouter()
note_routes.register(r'notes',NoteViewset , basename='note')


urlpatterns = [
    path('',include(note_routes.urls)) ,
    
]


