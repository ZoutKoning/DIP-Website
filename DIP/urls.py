from django.urls import path
from . import views
#comment
urlpatterns = [
    path('', views.index, name='index.html'),
]
