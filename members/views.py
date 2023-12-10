from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterUserForm

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ("There was an error with your signin. Please try again"))
            return redirect('login_user')
    else:
        return render(request, 'authenticate/auth_signin.html', {})


def logout_user(request):
    logout(request)
    return redirect('index')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            if request.POST:
                temp = request.POST['role_field']
                print(temp)
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Sign Up Successful")
            return redirect('dashboard')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/newUser.html', {'form': form})
