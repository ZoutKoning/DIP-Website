from auditlog.models import LogEntry
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import mysprint
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from members.models import Account
from auditlog.models import LogEntry


# Generate audit log pdf
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

<<<<<<< HEAD
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
=======
>>>>>>> d6c9feded8c11fb9a5350c1cc61e81cdb0ba35f1



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
def points(request):
    return render(request, "wallet.html")


# Sponsor application(PDF) page
def sponsors(request):
    #sponsorsinfo = Account.objects.all()
    return render(request, "sponsors.html")


# Dashboard page
def dashboard(request):
    return render(request, 'dashboard.html')


# Catalog page
def catalog(request):
    return render(request, "catalog.html")


# Page that loads the cart
def cart(request):
    return render(request, "cart.html")


def drivers(request):
    return render(request, "drivers.html")

