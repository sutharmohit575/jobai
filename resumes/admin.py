from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'ai_score', 'analyzed', 'uploaded_at']
    list_filter = ['analyzed']
