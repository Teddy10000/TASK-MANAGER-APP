from django.contrib import admin
from .models import Notes , Sharing

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('user','id','time_created')
    list_filter = ('user',)
    
    
    
admin.site.register(Notes,NoteAdmin)



class SharingAdmin(admin.ModelAdmin):
    
    list_display = ('id','shared_by','shared_with')
    
admin.site.register(Sharing,SharingAdmin)