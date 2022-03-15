from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AdminNote(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    number = models.IntegerField()
    des = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.name)
