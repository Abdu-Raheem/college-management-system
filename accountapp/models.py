from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    user_type = models.CharField(
        max_length=20,
        choices=[
            ('student', 'Student'),
            ('tutor', 'Tutor'),
            ('hod', 'HOD'),
            ('principal', 'Principal'),
        ],
        default='student'
    )
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)


class Profile(models.Model):    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True, null=True)
    house_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.id} - {self.user.user_type}"
    