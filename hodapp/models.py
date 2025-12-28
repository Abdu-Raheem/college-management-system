from django.db import models
from django.core.exceptions import ValidationError
from principalapp.models import Department


class HODTutors(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    hod = models.ForeignKey("accountapp.Profile", on_delete=models.CASCADE, related_name='hod_tutors')
    tutor = models.ForeignKey("accountapp.Profile", on_delete=models.CASCADE, related_name='tutors_assigned_by_hod')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'hod_tutors'
        unique_together = [['hod', 'tutor']]
        indexes = [
            models.Index(fields=['hod', 'tutor']),
        ]
    
    def clean(self):
        # Validate that hod has HOD role
        if self.hod.role != 'HOD':
            raise ValidationError('Only HODs can assign tutors.')
        
        # Validate that tutor has TUTOR role
        if self.tutor.role != 'TUTOR':
            raise ValidationError('Only tutors can be assigned by HOD.')
        
        # Validate that HOD and tutor belong to the same department
        try:
            hod_department = self.hod.department
            tutor_subjects = self.tutor.tutor_subjects.all()
            if tutor_subjects.exists():
                tutor_departments = {ts.subject.department for ts in tutor_subjects}
                if hod_department not in tutor_departments:
                    raise ValidationError('HOD and tutor must belong to the same department.')
        except Department.DoesNotExist:
            raise ValidationError('HOD must be assigned to a department.')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.hod.name} -> {self.tutor.name}"