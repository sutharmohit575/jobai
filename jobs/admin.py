from django.contrib import admin
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'job_type', 'level', 'is_active', 'created_at']
    list_filter = ['job_type', 'level', 'is_active']
    search_fields = ['title', 'company', 'skills_required']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'status', 'match_score', 'applied_at']
    list_filter = ['status']

admin.site.site_header = "JobAI Admin"        # Top header
admin.site.site_title = "JobAI Panel"         # Browser tab title
admin.site.index_title = "Welcome to JobAI"   # Dashboard title