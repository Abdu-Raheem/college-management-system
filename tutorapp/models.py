from django.db import models
from accountapp.models import Profile


class TutorStudents(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    tutor_id = models.ForeignKey(Profile, on_delete=models.CASCADE) # tutor ids
    student_id = models.ForeignKey(Profile, on_delete=models.CASCADE) # student ids
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TutorSubjects(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    tutor_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)