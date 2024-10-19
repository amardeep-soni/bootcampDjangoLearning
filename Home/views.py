from django.http import HttpResponse
from django.shortcuts import render

from .models import Home, Service, Testimonial


# Create your views here.
def index(request):
    data = Home.objects.all()
    service = Service.objects.all()
    testimonial = Testimonial.objects.all()
    context = {"data": data, "services": service, "testimonials": testimonial}

    return render(request, "index.html", context)
