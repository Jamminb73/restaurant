from django.shortcuts import render, get_object_or_404
from .models import Beef


def beef(request):
    beefs = Beef.objects
    return render(request, 'beef/beef.html', {'beefs':beefs})

def bigbeef(request, beef_id):
    bigbeefsum =  get_object_or_404(Beef, pk=beef_id)
    return render(request, 'beef/bigbeef.html', {'beef':bigbeefsum} )
