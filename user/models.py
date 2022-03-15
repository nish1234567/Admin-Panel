import email
from re import T
from tkinter import N
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from numpy import number
# Create your models here.
class Note(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    number = models.IntegerField()
    des = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.name)
