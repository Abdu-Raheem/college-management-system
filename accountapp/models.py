from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .manager import CustomUserManager


# class CustomUser(AbstractUser):
#     user_type = models.CharField(
#         max_length=20,
#         choices=[
#             ('student', 'Student'),
#             ('tutor', 'Tutor'),
#             ('hod', 'HOD'),
#             ('principal', 'Principal'),
#         ],
#         default='student'
#     )
#     profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
#     groups = models.ManyToManyField(Group, blank=True)
#     user_permissions = models.ManyToManyField(Permission, blank=True)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=[
        ('student', 'Student'), 
        ('tutor', 'Tutor'), 
        ('hod', 'HOD'), 
        ('principal', 'Principal')
    ], default='student')
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


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
    