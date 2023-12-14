from django.urls import path
from . import views
from django.contrib import messages
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('points/', views.points, name="points"),
    #path('login/', views.login, name="login"),
    # path('signup.html', views.signin, name="signin"),
    path('sponsors/', views.sponsors, name="sponsors"),
    path('drivers/', views.drivers, name="drivers"),
    path('dashboard/', views.dashboard, name="dashboard"),
    # URL path to the catalog
    path('catalog/', views.catalog, name="catalog"),
    # URL path to the cart
    path('cart/', views.cart, name="cart"),
<<<<<<< HEAD
     path('logs_report', views.logs_report, name='view_logs'),
=======
    path('logs_report', views.logs_report, name='view_logs'),
>>>>>>> d6c9feded8c11fb9a5350c1cc61e81cdb0ba35f1
]
