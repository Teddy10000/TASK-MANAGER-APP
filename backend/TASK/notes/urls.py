# from rest_framework import routers
from rest_framework_nested import routers
from .views import NoteViewset , ShareViewset
from django.urls import path ,include





## CHANGED TO NESTED ROUTERS 
note_routes = routers.SimpleRouter()
note_routes.register(r'notes',NoteViewset , basename='note')

share_routes = routers.SimpleRouter()
share_routes.register(r'share',ShareViewset,basename ='share')

urlpatterns = [
    path('',include(note_routes.urls)) ,
    path('', include(share_routes.urls)),
    
]


