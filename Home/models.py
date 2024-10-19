from django.db import models
from django.db import models


# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    resume_file = models.FileField(upload_to="results/")
    image = models.ImageField(upload_to="pictures/")
    about_me = models.TextField()


class Service(models.Model):
    service_icon = models.CharField(max_length=100)
    service_title = models.CharField(max_length=100)
    service_desc = models.TextField()


class Testimonial(models.Model):
    image = models.ImageField(upload_to="pictures/")
    name = models.CharField(max_length=100)
    message = models.TextField()
    compnay_position = models.CharField(max_length=100)

class Education(models.Model):
    start_month_year = models.CharField(max_length=100)
    end_month_year = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    Institue_name = models.CharField(max_length=100)

class Experience(models.Model):
    start_month_year = models.CharField(max_length=100)
    end_month_year = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
