from django.db import models
from accountapp.models import Profile


class HODDepartment(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    hod_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HODTutors(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    hod_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tutor_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)