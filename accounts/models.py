from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [('seeker', 'Job Seeker'), ('recruiter', 'Recruiter')]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='seeker')
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    company = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_seeker(self):
        return self.role == 'seeker'

    def is_recruiter(self):
        return self.role == 'recruiter'

    def __str__(self):
        return f"{self.username} ({self.role})"
