from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'group']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['title', 'author', 'price']