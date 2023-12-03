from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Role


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    Role = forms.CharField(max_length=1, help_text='D(driver) S(sponsor) A(admin)')
    # userRole = forms.ModelChoiceField(queryset=Role.objects.all())

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'username', 'password1', 'password2', 'Role')
