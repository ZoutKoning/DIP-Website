from django.db import models
from django.urls import reverse

# Create your models here

class DIP (models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

class Sprint (models.Model):
    sprint = models.CharField(max_length=250, help_text= 'current sprint')
    sprint_info = models.TextField()
    def __str__(self):
        """string for sprint"""
        return f' {self.sprint},{self.sprint_info}'


class User (models.Model):

    user_ID = models.IntegerField()

class User (models.Model):

    user_ID = models.IntegerField(primary_key=True)

    user_FName = models.CharField(max_length = 250)
    user_LName = models.CharField(max_length= 250)
    user_Password = models.CharField(max_length= 250)
    user_LoginName = models.CharField(max_length= 250)
    user_Type = models.CharField(max_length=1)


class Driver (models.Model):
    user_ID = models.ForeignKey(User,on_delete=models.CASCADE)
    wallet = models.CharField(max_length=250)

class Sponsor (models.Model):
     user_ID = models.ForeignKey(User,on_delete=models.CASCADE)
     sponsorCo = models.CharField(max_length=250)


class Admin(models.Model):
    user_ID = models.ForeignKey(User,on_delete=models.CASCADE)
    reportType = models.CharField(max_length=250)

