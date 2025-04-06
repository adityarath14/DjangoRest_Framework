from django.shortcuts import render
from travello.models import Destinations
# Create your views here.
def index(request):
    dests=Destinations.objects.all()
    return render(request, 'index.html', {'dests':dests})