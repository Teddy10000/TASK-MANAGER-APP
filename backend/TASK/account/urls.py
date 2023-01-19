from django.urls import path ,include
from . import views

#The simple jwt auhentication model
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )


urlpatterns = [

    path('',views.getRoute) ,
    # Giving the url location of the tokin pairs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
            ]