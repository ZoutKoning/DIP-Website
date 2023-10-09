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
