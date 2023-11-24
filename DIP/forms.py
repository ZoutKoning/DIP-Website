from django import forms
from .models import MyModel


# user input forms here

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ["fullname", "mobile_number", ]
        labels = {'fullname': "Name", "mobile_number": "Mobile Number", }
