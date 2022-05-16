from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=255 , null= True , blank= True)
    raiting = models.IntegerField(default= 0)
    reviewer = models.ForeignKey(get_user_model() , on_delete= models.CASCADE)


    def __str__(self) :
        return self.name

    def  get_absolute_url(self):
        return reverse('things_detail' , kwargs= {'pk' :self.pk})