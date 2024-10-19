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

