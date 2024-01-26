from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#make a table

class Topic(models.Model):
    name= models.CharField(max_length=200)

    def __str__(sekf):
        return self.name

class Room(models.Model):
    #id:
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants:
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
         return self.body[0:50]