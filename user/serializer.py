from dataclasses import field
from matplotlib.pyplot import cla
from rest_framework import serializers
from rest_framework.serializers import *
from .models import *
#from django.contrib.auth.views import User

class UserSerializer(serializers.ModelSerializer):
    def validate(self,data):
        username = data.get('username')
        email = data.get('email')
        if User.objects.filter(username=username).exists():
            raise ValidationError('This username is already exists')
        if User.objects.filter(username=username).exists():
            raise ValidationError('This email is already exists')
        return data

    class Meta:
        model = User
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

