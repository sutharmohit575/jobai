from django import forms
from .models import Job, Application

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'job_type', 'level', 'description', 'requirements', 'skills_required', 'salary_min', 'salary_max', 'deadline']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'requirements': forms.Textarea(attrs={'rows': 5}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell the recruiter why you are a great fit...'})
        }
