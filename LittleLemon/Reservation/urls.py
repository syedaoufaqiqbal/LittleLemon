from django.contrib import admin 
from django.urls import path 
from .views import booking ,registration

  
urlpatterns = [ 
    path('bookings',booking),
    path('registration',booking),
]