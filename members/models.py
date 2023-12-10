from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Role(models.Model):
    userRole = models.CharField(max_length=7)

    def __str__(self):
        return self.userRole


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=7)


''' ALMOST GOT IT PERFECT
class User(AbstractUser):
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=7)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)'''
