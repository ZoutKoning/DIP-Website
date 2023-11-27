from django.shortcuts import render

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
# Driver application(PDF) page
def drivers(request):
    return render(request, "drivers.html")
# Dashbaord page
def dashboard(request):
    return render(request, "dashboard.html")

# Catalog page
def catalog(request):
    return render(request, "catalog.html")

# Page that loads the cart
def cart(request):
    return render(request, "cart.html")
