from django.db import models


class Profile(models.Model):
    ROLE_CHOICES = [
        ('STUDENT', 'Student'),
        ('TUTOR', 'tutor'),
        ('HOD', 'head of department'),
        ('PRINCIPAL', 'principal'),
    ]
    
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Admin')
    phone = models.CharField(max_length=15)
    house_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_role_display()}"
    
    class Meta:
        db_table = 'profile'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['role']),
            models.Index(fields=['email']),
        ]