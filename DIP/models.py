from django.db import models

# Create your models here

class DIP (models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
