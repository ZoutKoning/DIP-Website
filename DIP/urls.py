from django.urls import path
from . import views
urlpatterns = [
    #URL path link to Index page ("home")
    path('', views.index, name="index"),
    #URL path link to About Page
    path('about/', views.about, name="about"),
    #URL path link to Wallet page
    path('wallet/', views.wallet, name ="wallet"),
    #URL path link to Application page(s)
    path('sponsors/', views.sponsors, name="sponsors"), #sponsor application
    path('drivers/', views.drivers, name="drivers"), #driver applicaiton
    path('dashboard/', views.dashboard, name="dashboard"),
    path('catalog/', views.catalog, name='catalog'),
    path('cart/', views.cart, name='cart')
]
