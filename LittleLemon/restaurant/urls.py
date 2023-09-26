from django.contrib import admin 
from django.urls import path 
from .views import BookingView,MenuView

  
urlpatterns = [ 
   path('bookings', BookingView.as_view(
        {	'get': 'list',
            'post': 'create',	
        })
	),
    path('bookings/<int:id>',BookingView.as_view(
        {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
        })
	),
    path('menu', MenuView.as_view(
        {	'get': 'list',
            'post': 'create',	
        })
	),
    path('menu/<int:id>',MenuView.as_view(
        {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
        })
	)
]