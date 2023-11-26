from django.db import models
from django.urls import reverse
import datetime
# Create your models here

class DIP (models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

class Sprint (models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    sprint = models.CharField(max_length=250, help_text= 'current sprint')
    sprint_info = models.TextField()
    def __str__(self):
        """string for sprint"""
        return f' {self.sprint},{self.sprint_info}'

class User (models.Model):

    user_ID = models.IntegerField(primary_key=True)
    
    user_FName = models.CharField(max_length = 250)
    user_LName = models.CharField(max_length= 250)
    user_Password = models.CharField(max_length= 250)
    user_LoginName = models.CharField(max_length= 250)
    user_Type = models.CharField(max_length=1)


# Model for USER SIGN UP.

class MyModel(models.Model):
    fullname = models.CharField(max_length= 200)
    mobile_number = models.IntegerField()

class mysprint(models.Model):
    teamNum = models.IntegerField()
    versNum = models.CharField(max_length=250)
    releaseDate = models.CharField(max_length=250)
    prodDesc = models.CharField(max_length=250)

    def __str__(self):
        return self.versNum
