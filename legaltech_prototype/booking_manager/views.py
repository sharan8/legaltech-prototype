from django.shortcuts import render, redirect

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
    return redirect('/booking_manager/')
