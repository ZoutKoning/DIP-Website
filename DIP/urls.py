from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('wallet/', views.wallet, name="wallet"),
<<<<<<< HEAD
    # URL path link to Application page(s)
    path('sponsors/', views.sponsors, name="sponsors"),  # sponsor application
    path('drivers/', views.drivers, name="drivers"), #signup page
    #url(r'form', views.drivers, name='form'),
    path('dashboard/', views.dashboard, name="dashboard")
    #checking things go usless comment
=======
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
>>>>>>> b5a94fd0b4f6b2f89b57f83a849ec2c8fe0c198c
]
