from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from accounts.models import User
from jobs.models import Job


class Command(BaseCommand):
    help = "Load demo data"

    def handle(self, *args, **kwargs):
        # USERS
        recruiter, created = User.objects.get_or_create(
            username='demo_recruiter',
            defaults={
                'email': 'recruiter@jobai.demo',
                'first_name': 'Priya',
                'last_name': 'Mehta',
                'role': 'recruiter',
                'company': 'JobAI Demo',
                'location': 'Bangalore',
                'password': make_password('demo1234'),
            }
        )
        self.stdout.write(f"{'Created' if created else 'Found'} recruiter")

        seeker, created = User.objects.get_or_create(
            username='demo_seeker',
            defaults={
                'email': 'seeker@jobai.demo',
                'first_name': 'Arjun',
                'last_name': 'Sharma',
                'role': 'seeker',
                'location': 'Bangalore',
                'bio': 'Full Stack Developer',
                'password': make_password('demo1234'),
            }
        )
        self.stdout.write(f"{'Created' if created else 'Found'} seeker")

        # JOBS RESET
        Job.objects.all().delete()

        jobs = [
            {"title": "Python Developer", "company": "Demo", "location": "India", "job_type": "full-time", "level": "entry", "skills_required": "Python", "salary_min": 500000, "salary_max": 1000000, "description": "Demo job", "requirements": "Basic Python"},
        ]

        for job in jobs:
            Job.objects.create(recruiter=recruiter, **job)

        self.stdout.write(self.style.SUCCESS("Demo data loaded successfully!"))