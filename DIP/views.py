from auditlog.models import LogEntry
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#imports for forms
#from decouple import config
#from . import decode_jwt
#import base64
#import requests
#from .forms import MyForm
from .models import mysprint

# imports for forms
from .models import NewUser
from .forms import NewUserForm
from .models import User
#from .forms import ReturnUser
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



def logs_report(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create Text Object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 8)

    # Add some lines of text
    # Designate the model
    logs = LogEntry.objects.all()
    # Create blank list
    lines = []
    # Write the log entries to lines
    for log_entry in logs:
        original_object = log_entry.object_repr
        changed_object = log_entry.changes
        lines.append(original_object)
        lines.append(changed_object)
        lines.append(" ")
        lines.append("===================")

    # Loop
    for line in lines:
        textob.textLine(line)

    # Finish up
    c.drawText(textob)

    c.showPage()
    c.save()
    buf.seek(0)

    # return file
    return FileResponse(buf, as_attachment=True, filename='Audit-Logs.pdf')

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


'''def signin(request):
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
    return render(request, 'signup.html', {'form': form, 'submitted': submitted})'''


'''def signup(request):
    submitted = False
    if request.method == "POST":
        form = ReturnUser(request.POST)
        if form.is_valid():
            try:
                p = UserInfo.objects.get('user_Return.firstName')
                return HttpResponseRedirect('/dashboard?submitted=True')
            except UserInfo.DoesNotExist:
                raise forms.ValidationError("User not exist.")
    else:
        form = ReturnUser
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'signin.html', {'form': form, 'submitted': submitted})'''


