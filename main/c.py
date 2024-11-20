import uuid
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

class Employee(models.Model):
    departement = models.CharField(max_length=100)
    project = models.ManytoManyField(Project)
    user = models.OneToOneField(User, on_delete=models.CASCADE)