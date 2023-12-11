from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterUserForm, ProfileForm, SponsorApplicationForm
from .models import UserProfile


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
        form_reg = RegisterUserForm(request.POST)
        form_prof = ProfileForm(request.POST)
        if form_reg.is_valid() and form_prof.is_valid():
            if request.POST:
                temp = request.POST['role_field']
                print(temp)
            new_user = form_reg.save()
            profile = form_prof.save(commit=False)
            if profile.user_id is None:
                profile.user_id = new_user.id
            username = form_reg.cleaned_data['username']
            password = form_reg.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Sign Up Successful")
            return redirect('dashboard')
    else:
        form_reg = RegisterUserForm()
        form_prof = ProfileForm()
    return render(request, 'authenticate/newUser.html',
                  {'form_reg': form_reg, 'form_prof': form_prof})