from django.shortcuts import render
from django.http import HttpResponse
from decouple import config
from . import decode_jwt
import base64
import requests
from .models import MyModel
from .forms import MyForm


# Home page
def index(request):
    return render(request, "index.html")


# About page
def about(request):
    return render(request, "about.html")


# Wallet page
def wallet(request):
    return render(request, "wallet.html")


# Sponsor application(PDF) page
def sponsors(request):
    return render(request, "sponsors.html")


# Signup page
def drivers(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = MyForm()
    return render(request, "drivers.html", {'form': form})


# Dashboard page
def dashboard(request):
    return render(request, "dashboard.html")


# Catalog page
def catalog(request):
    return render(request, "catalog.html")

# Page that loads the cart
def cart(request):
    return render(request, "cart.html")
