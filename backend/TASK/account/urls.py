from django.urls import path ,include
from . import views
from . views import MyTokenObtainPairView 


#The simple jwt auhentication model
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    )


urlpatterns = [

    path('',views.getRoute) ,
    # Giving the url location of the tokin pairs
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
            ]
