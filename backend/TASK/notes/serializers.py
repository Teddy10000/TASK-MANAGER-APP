from rest_framework import serializers
from .models import Notes ,Sharing




class TaskSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Notes
        fields = "__all__"
        
        
class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sharing
        
        fields = "__all__"
        
        




        
        
        
