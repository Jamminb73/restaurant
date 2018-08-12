from django.shortcuts import render, get_object_or_404
from .models import Pork

def pork(request):
    porks = Pork.objects
    return render(request, 'pork/pork.html', {'porks':porks})

def bigpork(request, pork_id):
    bigporksum = get_object_or_404(Pork, pk=pork_id)
    return render(request, 'pork/bigpork.html', {'pork':bigporksum} )
