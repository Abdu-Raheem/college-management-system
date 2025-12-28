from django.db import models
from django.core.exceptions import ValidationError
from accountapp.models import Profile
from principalapp.models import Subject


class EnrolledSubject(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'enrolled_subject'
        unique_together = [['student', 'subject']]
        indexes = [
            models.Index(fields=['student', 'subject']),
        ]
    
    def clean(self):
        # Validate that student has STUDENT role
        if self.student.role != 'STUDENT':
            raise ValidationError('Only students can enroll in subjects.')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.student.name} - {self.subject.subject_name}"


class ExamResult(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'exam_result'
        unique_together = [['student', 'subject']]
        indexes = [
            models.Index(fields=['student', 'subject']),
        ]
    
    def clean(self):
        # Validate that student has STUDENT role
        if self.student.role != 'STUDENT':
            raise ValidationError('Only students can have exam results.')
        
        # Validate that student is enrolled in the subject
        if not EnrolledSubject.objects.filter(student=self.student, subject=self.subject).exists():
            raise ValidationError('Student must be enrolled in the subject to have exam results.')
        
        # Validate marks range
        if self.marks < 0 or self.marks > 100:
            raise ValidationError('Marks must be between 0 and 100.')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.student.name} - {self.subject.subject_name}: {self.grade}"

