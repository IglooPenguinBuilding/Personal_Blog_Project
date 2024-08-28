from django.db import models

# Create your models here.
from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    summary = models.TextField()

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    graduation_date = models.DateField()

class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=20)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    url = models.URLField(blank=True)