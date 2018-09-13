from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Problem


def index(request):
##    neighbor_dispute = Problem()
##    neighbor_dispute.name = "Neighbor Dispute"
##    neighbor_dispute.coa = "You need to fill up a form in English"
##    neighbor_dispute.save()
    return render(request, 'english/index.html')


def coa_view(request):
    coa_object = Problem.objects.get(name="Neighbor Dispute")
    context = {
        'coa_object': coa_object
    }
    print(context)
    return render(request, 'english/sample_coa.html', context)

def next(request, paths_id):
    next_action = Problem.objects.get(pk=paths_id)
    if next_action.booking_manager:
        return redirect('/booking_manager')
    elif next_action.link:
        print("hi")
        return HttpResponseRedirect(next_action.link)
    else:
        context = {
            'next_action': next_action
        }
        return render(request, 'english/sample_coa.html', context)
