from django.shortcuts import render

# Create your views here.
def vuelos(request):
    template= "./content/flights.html"
    return render(request, template, {})