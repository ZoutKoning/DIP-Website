from django import forms
from django.forms import ModelForm
from .models import NewUser
from .models import User


# New User Form
class NewUserForm(ModelForm):
    class Meta:
        model = NewUser
        fields = ('firstName', 'lastName', 'email', 'username', 'password', 'role')


'''class ReturnUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('user_Return.firstName')'''