from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class AdminRegister(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request):
        serializer = UserAdminSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'Msg':'Admin user has created'})
        return Response(serializer.errors)

class AdminLogin(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({'Msg':'You have LogedIn'})
        return Response({'Msg':'Enter correct username or password'})

class AdminProfile(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        user = request.user
        stu = User.objects.get(id = user.id)
        serializer = UserAdminSerializer(stu)
        return Response(serializer.data)

    def put(self,request,pk):
        stu = User.objects.get(id=pk)
        serializer = UserAdminSerializer(instance=stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Admin Profile has updated'})
        return Response(serializer.errors)

    def delete(self,request,pk):
        stu = User.objects.get(id=pk)
        stu.delete()
        return Response({'Msg':'Admin User has deleted'})

class AdminUserNote(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        stu = AdminNote.objects.all()
        serializer = AdminNoteSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AdminNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Note has created'})
    
    def delete(self,request,pk):
        stu = AdminNote.objects.get(id=pk)
        stu.delete()
        return Response({'Msg':'Note has deleted'})