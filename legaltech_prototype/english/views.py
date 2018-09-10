from django.shortcuts import render

from .models import Problem


def index(request):
    neighbor_dispute = Problem()
    neighbor_dispute.name = "Neighbor Dispute"
    neighbor_dispute.coa = "You need to fill up a form in English"
    neighbor_dispute.save()
    return render(request, 'english/index.html')


def coa_view(request):
    coa_object = Problem.objects.filter(name="Neighbor Dispute")
    context = {
        'coa_object': coa_object
    }
    return render(request, 'english/coa.html', context)
