from rest_framework import serializers
from .models import Notes

class TaskSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    
    
    class Meta:
        model = Notes
        fields = ('id', 'username', 'title', 'description', 'time_created', 'time_now')
        read_only_fields = ('id', 'time_created', 'time')