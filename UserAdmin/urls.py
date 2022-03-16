from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('gettoken',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken',TokenRefreshView.as_view(),name='token_refresh'),
    path('verifytoken',TokenVerifyView.as_view(),name='token_verify'),
    path('adminregister/', AdminRegister.as_view()),
    path('adminlogin',AdminLogin.as_view()),
    path('adminprofile',AdminProfile.as_view()),
    path('adminprofile/<int:pk>',AdminProfile.as_view()),
    path('adminusernote',AdminUserNote.as_view()),
    path('adminusernote/<int:pk>',AdminUserNote.as_view()),

    ]
