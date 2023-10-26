from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index.html'),
    path('', views.login, name='login.html'),
    path('', views.signup, name='signup.html')
]
