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
