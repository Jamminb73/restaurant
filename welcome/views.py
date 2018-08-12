from django.shortcuts import render

def home(request):
    return render(request, 'welcome/home.html')

def contact(request):
    return render(request, 'welcome/contact.html')

def about(request):
    return render(request, 'welcome/about.html')
