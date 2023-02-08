
# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
   
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    username = models.CharField(max_length = 40,blank = True)
    full_name = models.CharField(max_length=40)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self) :
        full_name = str(self.first_name + self.last_name )
        return full_name