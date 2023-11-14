from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

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

def cognito_login(request):
    id_token = request.POST.get('id_token') #Gets id token
    user = authenticate(request, id_token=id_token)
    if user:
        login(request, user)
        #Redirect or respond accordingly upon successful authentication
        return HttpResponse('Authenticated')
    else:
        return HttpResponse('Authentication failed')