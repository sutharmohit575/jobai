from django.db import models
from django.conf import settings

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resumes')
    title = models.CharField(max_length=100, default='My Resume')
    file = models.FileField(upload_to='resumes/')
    raw_text = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    experience_years = models.FloatField(default=0)
    education = models.TextField(blank=True)
    ai_summary = models.TextField(blank=True)
    ai_score = models.FloatField(default=0)
    ai_suggestions = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    analyzed = models.BooleanField(default=False)

    def get_skills_list(self):
        return [s.strip() for s in self.skills.split(',') if s.strip()]

    def __str__(self):
        return f"{self.user.username} - {self.title}"


class ResumeBuilder(models.Model):
    TEMPLATE_CHOICES = [
        ('modern', 'Modern'),
        ('classic', 'Classic'),
        ('minimal', 'Minimal'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='built_resumes')
    title = models.CharField(max_length=100, default='My Resume')
    template = models.CharField(max_length=20, choices=TEMPLATE_CHOICES, default='modern')

    # Personal Info
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    website = models.URLField(blank=True)

    # Content sections (stored as JSON text)
    summary = models.TextField(blank=True)
    experience = models.TextField(blank=True, default='[]')  # JSON
    education = models.TextField(blank=True, default='[]')   # JSON
    skills = models.TextField(blank=True)
    projects = models.TextField(blank=True, default='[]')    # JSON
    certifications = models.TextField(blank=True)

    # AI enhancement flags
    ai_enhanced = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} — {self.title}"
