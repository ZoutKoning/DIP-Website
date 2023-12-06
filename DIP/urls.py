from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('wallet/', views.wallet, name="wallet"),
    # URL path link to Application page(s)
    path('sponsors/', views.sponsors, name="sponsors"),
    path('drivers/', views.drivers, name="drivers"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.login, name="login"),
    path('signup.html', views.signup, name="signup"),
    path('signin.html', views.signin, name="signin"),
    path('sponsors/', views.sponsors, name="sponsors"),
    path('drivers/', views.drivers, name="drivers"),
    path('dashboard/', views.dashboard, name="dashboard"),
    # URL path to the catalog
    path('catalog/', views.catalog, name="catalog"),
    # URL path to the cart
    path('cart/', views.cart, name="cart")
]
