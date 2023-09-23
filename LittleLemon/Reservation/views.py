from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Booking
from .models import Registration
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# Create your views here.
@csrf_exempt
def booking(request):
    if request.method == 'GET':
        bookings = Booking.objects.all().values()
        return JsonResponse({"bookings":list(bookings)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        booking = Booking(
            title = title,
            author = author,
            price = price
        )
        try:
            booking.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return JsonResponse(model_to_dict(booking), status=201)
    
@csrf_exempt
def registration(request):
    if request.method == 'GET':
        registrations = Registration.objects.all().values()
        return JsonResponse({"registrations":list(registrations)})
    elif request.method == 'POST':
        url = request.POST.get('url')
        username = request.POST.get('username')
        email = request.POST.get('email')
        group = request.POST.get('group')
        registration = Registration(
            url = url,
            username = username,
            email = email,
            group=group
        )
        try:
            registration.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return JsonResponse(model_to_dict(registration), status=201)    