from django.db import models
from account.models import  *

# Create your models here.

class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name="user", blank=False, null=False,on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True, blank=False, null=False) 
    title = models.CharField(max_length=30, blank=False, null=True,default=None)
    time_to_complete = models.DateTimeField(blank=True , default =None)
    description = models.TextField(max_length=255, blank=True, null=False)
    attachments = models.ImageField(blank=True, null=False)
    details = models.CharField(max_length  = 255 , null=False, default = None)
    completed = models.BooleanField(default=False, null=True, blank=False)
    
    def __str__(self):
        return self.title
    
    
    
   # For the category entitle 
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=True)
    title = models.ForeignKey(Notes, blank=False, null=False,on_delete =models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Sharing(models.Model):
    id = models.AutoField(primary_key=True)
    note = models.ForeignKey(Notes, on_delete=models.CASCADE)
    shared_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='shared_by')
    shared_with = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='shared_with')
    shared_at = models.DateTimeField(auto_now_add=True)
    
    
    
    
    
    
    
    
    
    
    
