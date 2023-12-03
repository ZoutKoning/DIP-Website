from django.db import models
from django.urls import reverse
import datetime


# Create your models here

class DIP(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()


class Sprint(models.Model):
    start_date = models.DateTimeField()
    sprint = models.CharField(max_length=250, help_text='current sprint')
    sprint_info = models.TextField()

    def __str__(self):
        """string for sprint"""
        return f' {self.sprint},{self.sprint_info}'


class NewUser(models.Model):
    firstName = models.CharField('first name', max_length=250)
    lastName = models.CharField('last name', max_length=250)
    email = models.EmailField('email')
    username = models.CharField('username', max_length=250)
    password = models.CharField('password', max_length=250)
    role = models.CharField('role', max_length=1, help_text='D(driver) S(sponsor) A(admin)')


class User(models.Model):
    user_ID = models.IntegerField(primary_key=True)
    user_Return = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    #user_LName = NewUser.lastName
    #user_Password = NewUser.password
    #user_LoginName = NewUser.username
    #user_Role = NewUser.role


class mysprint(models.Model):
    teamNum = models.IntegerField()
    versNum = models.CharField(max_length=250)
    releaseDate = models.CharField(max_length=250)
    prodDesc = models.CharField(max_length=250)

    def __str__(self):
        return self.versNum


