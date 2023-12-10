from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


DRIVER = 1
SPONSOR = 2
ADMIN = 3
ROLE_CHOICES = (
    (DRIVER, "driver"),
    (SPONSOR, "sponsor"),
    (ADMIN, "admin"),
)


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'role')
