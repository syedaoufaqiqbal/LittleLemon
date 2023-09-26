from .models import Booking
from .models import Menu
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
 

class BookingView(ViewSet):
    def list(self, request):
      return Response({"message":"All bookings"}, status.HTTP_200_OK)
    def create(self, request):
      return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
    def update(self, request, id=None):
     return Response({"message":"Updating a book"}, status.HTTP_200_OK)
    def retrieve(self, request, id=None):
     return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
    def partial_update(self, request, id=None):
     return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
    def destroy(self, request, id=None):
      return Response({"message":"Deleting a book"}, status.HTTP_200_OK)
  
  
class MenuView(ViewSet):
    def list(self, request):
      return Response({"message":"All menues"}, status.HTTP_200_OK)
    def create(self, request):
      return Response({"message":"Creating a menu"}, status.HTTP_201_CREATED)
    def update(self, request, id=None):
     return Response({"message":"Updating a menu"}, status.HTTP_200_OK)
    def retrieve(self, request, id=None):
     return Response({"message":"Displaying a menu"}, status.HTTP_200_OK)
    def partial_update(self, request, id=None):
     return Response({"message":"Partially updating a menu"}, status.HTTP_200_OK)
    def destroy(self, request, id=None):
      return Response({"message":"Deleting a menu"}, status.HTTP_200_OK)