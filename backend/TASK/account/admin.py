from django.contrib import admin

# Register your models here.
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    
    list_display = ('username', 'email', 'is_active',
                    'is_staff', 'is_superuser', 'last_login',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    readonly_fields = ["date_joined"]
    #n Django, the fieldsets option in the admin class is used to control the layout of the fields in the admin interface. It is a list of tuples, where each tuple defines a fieldset. Each tuple is composed of two elements:
    fieldsets = (
        ('Information', {'fields': ('username', 'email','first_name','last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email','first_name' , 'last_name','password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)