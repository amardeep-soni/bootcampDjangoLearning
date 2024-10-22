from django.db import models
from django.db import models


# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    resume_file = models.FileField(upload_to="results/")
    image = models.ImageField(upload_to="pictures/")
    about_me = models.TextField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    facebook_link = models.CharField(max_length=200)
    linkedin_link = models.CharField(max_length=200)
    instagram_link = models.CharField(max_length=200)
    github_link = models.CharField(max_length=200)


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

class Projects(models.Model):
    image = models.ImageField(upload_to="pictures/project")
    name = models.CharField(max_length=100)
    languages_used = models.CharField(max_length=100)
    repo_link  = models.CharField(max_length=200)
    live_link = models.CharField(max_length=200)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
