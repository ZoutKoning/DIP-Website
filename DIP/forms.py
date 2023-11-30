from django import forms
from django.forms import ModelForm
from .models import NewUser
from .models import User


# New User Form
class NewUserForm(ModelForm):
    class Meta:
        model = NewUser
        fields = ('firstName', 'lastName', 'email', 'username', 'password', 'role')



class ReturnUser(ModelForm):
    class Meta:
        model = User
        fields = ('user_LoginName','user_Password')
