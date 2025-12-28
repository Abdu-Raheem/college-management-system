from django.db import models
from accountapp.models import Profile


class Department(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    department_name = models.CharField(max_length=100)
    department_description = models.TextField()
    hod_id = models.OneToOneField(Profile)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
