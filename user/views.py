from functools import partial
from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from user import serializer
# Create your views here.
class Register(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email)
        user.set_password(password)
        user.save()
        return Response({'Msg':'You have successfully registered'})

class Login(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({'Msg':'You have LogedIn'})
        return Response({'Msg':'Enter correct username or password'})

class Profile(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    def get(self,request):
        user = request.user
        stu = User.objects.get(id = user.id)
        serializer = UserSerializer(stu)
        return Response(serializer.data)

    def put(self,request,pk):
        stu = User.objects.get(id=pk)
        serializer = UserSerializer(instance=stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Profile has updated'})
        return Response(serializer.errors)

    def delete(self,request,pk):
        stu = User.objects.get(id=pk)
        stu.delete()
        return Response({'Msg':'User has deleted'})

class UserNote(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    def get(self,request):
        stu = Note.objects.all()
        serializer = NoteSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Note has created'})
    
    def delete(self,request,pk):
        stu = Note.objects.get(id=pk)
        stu.delete()
        return Response({'Msg':'Note has deleted'})