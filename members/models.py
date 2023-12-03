from django.db import models
from django.urls import reverse


# Create your models here.

class Role(models.Model):
    userRole = models.CharField(max_length=7)

    def __str__(self):
        return self.userRole
