from django.shortcuts import render

# Create your views here.

def medicines(request):
    return render(request, 'medicines.html')