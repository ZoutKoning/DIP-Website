from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Account

# ROLE CHOICES
DRIVER = "driver"
SPONSOR = "sponsor"
ADMIN = "admin"
ROLE_CHOICES = (
    (DRIVER, "driver"),
    (SPONSOR, "sponsor"),
    (ADMIN, "admin"),
)

# SPONSOR CHOICES
AMAZON = "Amazon"
YOUTUBE = "YouTube"
MICROSOFT = "Microsoft"
NONE = "NONE"
SPONSOR_CHOICES = (
    (AMAZON, "Amazon"),
    (YOUTUBE, "YouTube"),
    (MICROSOFT, "Microsoft"),
    (NONE, "NONE"),
)


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class AccountForm(forms.ModelForm):
    role_field = forms.ChoiceField(choices=ROLE_CHOICES)
    sponsor_field = forms.ChoiceField(choices=SPONSOR_CHOICES)

    class Meta:
        model = Account
        fields = ('role_field', 'sponsor_field',)


class SponsorApplicationForm(forms.ModelForm):
    sponsor_field = forms.ChoiceField(choices=SPONSOR_CHOICES)

    class Meta:
        model = Account
        fields = ('sponsor_field',)
