from django.http import HttpResponse
from django.shortcuts import render

from .models import Home, Service


# Create your views here.
def index(request):
    data = Home.objects.all()
    service = Service.objects.all()
    return render(request, "index.html", {"data": data, "services": service})
