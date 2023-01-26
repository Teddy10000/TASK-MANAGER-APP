from rest_framework import routers
from .views import NoteViewset



urlpatterns = []


routes = routers.DefaultRouter()
routes.register(r'notes',NoteViewset,basename='Notes')

urlpatterns += routes.urls
