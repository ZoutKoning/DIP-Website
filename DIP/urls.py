from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('wallet/', views.wallet, name ="wallet"),
    path('sponsors/', views.sponsors, name="sponsors"),
    path('drivers/', views.drivers, name="drivers")
]
