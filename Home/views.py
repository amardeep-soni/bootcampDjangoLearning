from django.http import HttpResponse
from django.shortcuts import render

from .models import Home, Service, Testimonial, Education, Experience, Projects


# Create your views here.
def index(request):
    data = Home.objects.all()
    service = Service.objects.all()
    testimonial = Testimonial.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    project = Projects.objects.all()
    context = {"data": data, "services": service, "testimonials": testimonial, "experiences": experience, "educations": education, "projects": project}

    return render(request, "index.html", context)
