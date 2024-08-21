from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView 

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='Token obtain'),
    path('TokenRefresh/', TokenRefreshView.as_view(), name='Token refresh') ,
    path('register/', UserResigter.as_view(),name="sign up")
]
