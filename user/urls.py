from os import name
from django.contrib import admin
from django.urls import path
from user.views import Login, Profile, Register, UserNote
from rest_framework_simplejwt.views import TokenObtainPairView,TokenVerifyView,TokenRefreshView

urlpatterns = [
    path('gettoken/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('verifytoken/',TokenVerifyView.as_view(),name='token_very_verify'),
    path('refreshtoken/s',TokenRefreshView.as_view(),name='token_refresh'),
    path('register/', Register.as_view()),
    path('login',Login.as_view()),
    path('profile',Profile.as_view()),
    path('profile/<int:pk>',Profile.as_view()),
    path('usernote',UserNote.as_view()),
    path('usernote/<int:pk>',UserNote.as_view()),
]
