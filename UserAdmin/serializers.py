from dataclasses import field
import email
from unicodedata import name
from wsgiref import validate
from rest_framework import serializers
from rest_framework.serializers import *
from django.contrib.auth.models import User

from UserAdmin.models import AdminNote

class UserAdminSerializer(serializers.ModelSerializer):
    def validate(self,data):
        username = data.get('username')
        email = data.get('password')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username is already exists')
        if User.objects.filter(email=email):
            raise ValidationError('Email is already exists')

    def create(self,validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        email = validated_data.get('email')
        username = validated_data.get('username')
        password = validated_data.get('password')
        user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,is_staff=True)
        user.set_password()
        user.save()
        return validated_data

class AdminNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminNote
        fields = '__all__'