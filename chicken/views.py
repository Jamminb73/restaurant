from django.shortcuts import render, get_object_or_404
from .models import Chicken

def chicken(request):
    chickens = Chicken.objects
    return render(request, 'chicken/chicken.html', {'chickens':chickens})

def bigchicken(request, chicken_id):
    bigchickensum = get_object_or_404(Chicken, pk=chicken_id)
    return render(request, 'chicken/bigchicken.html', {'chicken':bigchickensum} )
