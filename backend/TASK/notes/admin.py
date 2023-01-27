from django.contrib import admin
from .models import Notes 

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('user','id','time_created')
    
    
    

admin.site.register(Notes,NoteAdmin)


