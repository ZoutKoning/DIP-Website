from django.db import models
from django.urls import reverse
import datetime
from auditlog.registry import auditlog
from members.models import UserProfile


# Create your models here


class DIP(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()


class NewUser(models.Model):
    firstName = models.CharField('first name', max_length=250)
    lastName = models.CharField('last name', max_length=250)
    email = models.EmailField('email')
    username = models.CharField('username', max_length=250)
    password = models.CharField('password', max_length=250)
    role = models.CharField('role', max_length=1, help_text='D(driver) S(sponsor) A(admin)')


class User(models.Model):
    user_ID = models.IntegerField(primary_key=True)
    # Commenting out line because of FK no null error
    # user_Return = models.ForeignKey(NewUser, on_delete=models.CASCADE)


class points(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE,)
    myPoints = models.IntegerField(default=100)


class mysprint(models.Model):
    teamNum = models.IntegerField()
    versNum = models.CharField(max_length=250)
    releaseDate = models.CharField(max_length=250)
    prodDesc = models.CharField(max_length=250)


auditlog.register(mysprint)
auditlog.register(User)
auditlog.register(NewUser)
auditlog.register(DIP)




