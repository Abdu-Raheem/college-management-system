from django.db import models
from django.core.exceptions import ValidationError
from accountapp.models import Profile


class Department(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    department_name = models.CharField(max_length=100)
    department_description = models.TextField()
    hod = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def clean(self):
        # Validate that hod has HOD role
        if self.hod and self.hod.role != 'HOD':
            raise ValidationError('Only users with HOD role can be assigned as Head of Department.')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.department_name
    
    class Meta:
        db_table = 'department'
        ordering = ['department_name']
        indexes = [
            models.Index(fields=['department_name']),
        ]


class Subject(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=100, unique=True)
    subject_description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.subject_name} ({self.subject_code})"
    
    class Meta:
        db_table = 'subject'
        ordering = ['subject_name']
