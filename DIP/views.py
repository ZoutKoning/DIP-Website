from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def wallet(request):
    return render(request, "wallet.html")
