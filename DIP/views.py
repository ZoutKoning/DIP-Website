from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import NewUser
from .forms import NewUserForm
from .models import mysprint

# imports for forms
from .models import NewUser
from .forms import NewUserForm
from .models import User
from .forms import ReturnUser


# Home page
def index(request):
    return render(request, "index.html")


# About page
def about(request):
    sprintInfo = mysprint.objects.all()

    return render(request, "about.html", {'sprintInfo': sprintInfo})


# Wallet page
def wallet(request):
    return render(request, "wallet.html")


# Sponsor application(PDF) page
def sponsors(request):
    return render(request, "sponsors.html")


def drivers(request):
    return render(request, "drivers.html")


# Dashboard page
def dashboard(request):
    return render(request, 'dashboard.html')


# Catalog page
def catalog(request):
    return render(request, "catalog.html")


# Page that loads the cart
def cart(request):
    return render(request, "cart.html")


# Sign In/Up page
def login(request):
    return render(request, 'login.html')


def signup(request):
    submitted = False
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard?submitted=True')
    else:
        form = NewUserForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'signup.html', {'form': form, 'submitted': submitted})


def signin(request):
    submitted = False
    if request.method == "POST":
        form = ReturnUser(request.POST)
        try:
            p = UserInfo.objects.get(id=your_id)
        except UserInfo.DoesNotExist:
            raise forms.ValidationError("User not exist.")
    return render(request, 'signin.html')


