from django.contrib.auth.models import User;
from .models import Booking
from .models import Menu
from rest_framework import serializers;

class UserSerializer(serializers.ModelSerializer):
    class Meta :
         model = User
         fields = ['url', 'username', 'email', 'groups'] 

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
          model = Menu
          fields = ['id', 'title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
         model = Booking
         fields = ['id','name', 'no_of_guests', 'bookingdate']