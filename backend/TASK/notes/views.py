from django.shortcuts import render
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import viewsets
from .serializers import *
from .models import *
from notifications.models import Notification 
from django.dispatch import receiver
from django.db.models.signals import post_save
from notifications.signals import notify 
from .models import Sharing


# Create your views here.

# I want to write a code so that i check if the user is a staff before
# before i hand over every note to the user, that's 
from rest_framework.decorators import authentication_classes, permission_classes

class CustomPermission(BasePermission):
    def has_permission(self,request,permission):
        if request.method in ["GET", "OPTIONS","HEAD"]:
            return True
        return request.user and request.user.is_staff
            


class NoteViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        #return Notes.objects.filter(user_id=self.request.user)
        queryset = Notes.objects.all()
        user_id = self.request.query_params.get("user_id", None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset
    
    
class ShareViewset(viewsets.ModelViewSet):
    serializer_class = ShareSerializer
    queryset = Sharing.objects.all()
    
    def perform_create(self, serializer):
            serializer.save(shared_by=self.request.user)
            shared_to = serializer.validated_data['shared_to']
            shareable_link = self.request.build_absolute_uri(serializer.data["note"])
            
            notify.send(self.request.user, recipient=shared_to, verb='shared a note', action_object=shareable_link)
    
    '''
    def create(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        shareable_link = self.request.build_absolute_uri(serializer.data["id"])
        shared_to = serializer.validated_data['shared_to']
        note = Notes.objects.get(pk='note_id')
        share = Sharing.objects.create(note=note, user=request.user)
        Notification.objects.create(
            recipient=shared_to,
            actor=self.request.user,
            verb='shared',
            target=note,
            description=f"{request.user} shared a note with you"
        )
        
        
        
        
        
        @receiver(post_save, sender=Sharing)
        def notify_share(sender, instance, created, **kwargs):
            if created:
                notify.send(
                    instance.user, 
                    recipient=instance.note.user, 
                    verb='shared', 
                    target=instance.note,
                    description=f"{instance.user} shared a note with you"
                )
                '''
            
        
        
''' headers = self.get_success_headers(serializer.data)
       # Only create a shareable link if the user toggles the share button
        if request.data["share"]:
            shareable_link = self.request.build_absolute_uri(serializer.data["id"])
            # Create a notification
            notification = self.create_notification(recipient=request.data["shared_with"], verb='shared', target=shareable_link)
            # Send the notification
            self.send_notification(notification)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        '''
    
   
   
    
    
    
    
    
