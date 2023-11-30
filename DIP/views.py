from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#imports for forms
#from decouple import config
#from . import decode_jwt
#import base64
#import requests
#from .forms import MyForm
from .models import NewUser
from .forms import NewUserForm
from .models import MyModel
from . models import mysprint


# Home page
def index(request):
        return render(request, 'index.html')



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


def signin(request):
    submitted = False
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login?submitted=True')
    else:
        form = NewUserForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'signup.html', {'form': form, 'submitted': submitted})


def signin(request):
    return render(request, 'signin.html')


'''
def getTokens(code):
    TOKEN_ENDPOINT = config('TOKEN_ENDPOINT')
    REDIRECT_URL = config('REDIRECT_URL')
    CLIENT_ID = config('CLIENT_ID')
    CLIENT_SECRET = config('CLIENT_SECRET')

    encodeData = base64.b64encode(bytes(f"{CLIENT_ID}:{CLIENT_SECRET}", "ISO-8859-1")).decode("ascii")

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {encodeData}'
    }

    body = {
        'grant_type': 'authorization-code',
        'client_id': CLIENT_ID,
        'code': code,
        'redirect_url': REDIRECT_URL,
    }

    response = requests.post(TOKEN_ENDPOINT, data=body, headers=headers)

    id_token = response.json()['id_token']

    userData = decode_jwt.lambda_handler(id_token, None)

    if not userData:
        return False

    user = {
        'id_token': id_token,
        'name': userData['name'],
        'email': userData['email'],
    }
    return user


def getSession(request):
    try:
        response = request.COOKIES["sessiontoken"]
        return response
    except:
        return None


def signout(request):
    response = render(request, 'index.html', {'status': 0})
    response.delete_cookie('sessiontoken')
    return response

'''
