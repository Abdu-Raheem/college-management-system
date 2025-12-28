from django.db import models
from django.core.exceptions import ValidationError
from principalapp.models import Subject


class TutorStudents(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    tutor = models.ForeignKey("accountapp.Profile", on_delete=models.CASCADE, related_name='tutor_students')
    student = models.ForeignKey("accountapp.Profile", on_delete=models.CASCADE, related_name='students_assigned_to_tutor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tutor_students'
        unique_together = [['tutor', 'student']]
        indexes = [
            models.Index(fields=['tutor', 'student']),
        ]
    
    def clean(self):
        # Validate that tutor has TUTOR role
        if self.tutor.role != 'TUTOR':
            raise ValidationError('Only tutors can be assigned to students.')
        
        # Validate that student has STUDENT role
        if self.student.role != 'STUDENT':
            raise ValidationError('Only students can be assigned to tutors.')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.tutor.name} -> {self.student.name}"


class TutorSubjects(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    tutor = models.ForeignKey("accountapp.Profile", on_delete=models.CASCADE)
    subject = models.ForeignKey("principalapp.Subject", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tutor_subjects'
        unique_together = [['tutor', 'subject']]
        indexes = [
            models.Index(fields=['tutor', 'subject']),
        ]
    
    def clean(self):
        # Validate that tutor has TUTOR role
        if self.tutor.role != 'TUTOR':
            raise ValidationError('Only tutors can teach subjects.')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.tutor.name} - {self.subject.subject_name}"