from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import boto3

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')  # redirect to the home page

        return render(request, 'login.html', {'error_message': 'Invalid login credentials'})  # render the login template with an error

    return render(request, 'login.html')  # render the login template

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        group = request.POST['group']  # drivers, admins, or sponsors

        client = boto3.client('cognito-idp', region_name ='us-east-1')
        try:
            response = client.sign_up(
                ClientId='24572ehjeno50ma5122ql3oumd',
                Username=username,
                Password=password,
                UserAttributes=[
                    {
                        'Name': 'email',
                        'Value': email
                    }
                ]
            )

            # Add user to the specified group regardless of confirmation status
            client.admin_add_user_to_group(
                UserPoolId='us-east-1_mwt8Tw8od',
                Username=username,
                GroupName=group
            )

            return redirect('login')  # Redirect to login view after successful signup

        except client.exceptions.ClientError as e:
            return render(request, 'signup.html', {'error_message': 'Error signing up. Try again.'})

    return render(request, 'signup.html')  # render the signup template

