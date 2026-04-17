from django.db import models
from django.conf import settings

class Job(models.Model):
    TYPE_CHOICES = [
        ('full-time', 'Full Time'), ('part-time', 'Part Time'),
        ('contract', 'Contract'), ('internship', 'Internship'), ('remote', 'Remote'),
    ]
    LEVEL_CHOICES = [
        ('entry', 'Entry Level'), ('mid', 'Mid Level'),
        ('senior', 'Senior Level'), ('lead', 'Lead/Manager'),
    ]
    recruiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posted_jobs')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='full-time')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='mid')
    description = models.TextField()
    requirements = models.TextField()
    skills_required = models.TextField(help_text='Comma-separated skills')
    salary_min = models.IntegerField(blank=True, null=True)
    salary_max = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)

    def get_skills_list(self):
        return [s.strip() for s in self.skills_required.split(',') if s.strip()]

    def __str__(self):
        return f"{self.title} @ {self.company}"

class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'), ('reviewing', 'Reviewing'),
        ('accepted', 'Accepted'), ('rejected', 'Rejected'),
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    resume = models.ForeignKey('resumes.Resume', on_delete=models.SET_NULL, null=True, blank=True)
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    match_score = models.FloatField(default=0.0)
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('job', 'applicant')

    def __str__(self):
        return f"{self.applicant.username} → {self.job.title}"
