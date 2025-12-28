from django.db import models
from accountapp.models import Profile


class EnrolledSubject(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=100)
    subject_description = models.TextField()
    student_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExamResult(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    student_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

