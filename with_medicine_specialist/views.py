from django.shortcuts import render

# Create your views here.

def specialist(request):
    return render(request, 'specialist.html')