from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


from .models import Location, Session

# Create your views here.

def index(request):
    locations = Location.objects.all()
    context = {
        'locations': locations,
    }
    return render(request, 'booking_manager/bookingmain.html', context)

def book(request, session_id):
    session = Session.objects.get(pk=session_id)
    session.status = 'Booked'
    session.save()
    return render(request, 'booking_manager/details.html')

def search(request, address):
    return HttpResponseRedirect("https://www.google.com/maps/search/"+address)
