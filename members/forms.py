from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Role


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    lastn_name = forms.CharField(max_length=100)
    Role = forms.CharField(max_length=1, help_text='D(driver) S(sponsor) A(admin)')
    # userRole = forms.ModelChoiceField(queryset=Role.objects.all())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'Role')
