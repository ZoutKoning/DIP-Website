from django.db import models
from django.urls import reverse
from datetime import date
from django.utils import timezone
# Create your models here

class DIP (models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

def start_date(self):
    started = date(2023, 9, 5)
    return started
        
def current_date(self):
    current = timezone.now().date()
    return current

class Sprint (models.Model):
    def current_sprint(self, start_date, current_date):
        sprint_num = (current_date - start_date) // 7
        return sprint_num
    
class User (models.Model):

    user_ID = models.IntegerField(primary_key=True)
    
    user_FName = models.CharField(max_length = 250)
    user_LName = models.CharField(max_length= 250)
    user_Password = models.CharField(max_length= 250)
    user_LoginName = models.CharField(max_length= 250)
    user_Type = models.CharField(max_length=1)


