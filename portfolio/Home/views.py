from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Contact, Home, Service, Testimonial, Education, Experience, Projects


# Create your views here.
def index(request):
    data = Home.objects.all()
    service = Service.objects.all()
    testimonial = Testimonial.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    project = Projects.objects.all()
    context = {
        "data": data,
        "services": service,
        "testimonials": testimonial,
        "experiences": experience,
        "educations": education,
        "projects": project,
    }

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print(name, email, subject, message)

        #   save the contact message to the database
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        return redirect('success')

    return render(request, "index.html", context)


def contact_success(request):
    return render(request, "contact_success.html")
