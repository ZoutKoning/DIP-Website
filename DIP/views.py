from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#imports for forms
#from .forms import MyForm
from .models import NewUser
from .forms import NewUserForm
from . models import mysprint
from . models import Wallet


# Home page
def index(request):
        return render(request, 'index.html')

# About page
def about(request):
    sprintInfo = mysprint.objects.all()

    return render(request, "about.html", {'sprintInfo': sprintInfo})


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
            return HttpResponseRedirect('/login?submitted=True')
    else:
        form = NewUserForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'signup.html', {'form': form, 'submitted': submitted})


def signin(request):
    return render(request, 'signin.html')


def wallet(request, user_id):
    user = get_object_or_404(NewUser, id=user_id)
    wallet = get_object_or_404(Wallet, user=user)

    context = {
        'user': user,
        'wallet': wallet
    }
    return render(request, 'wallet.html', context)
