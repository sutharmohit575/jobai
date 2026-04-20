# Generated migration for ResumeBuilder model

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeBuilder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='My Resume', max_length=100)),
                ('template', models.CharField(
                    choices=[('modern', 'Modern'), ('classic', 'Classic'), ('minimal', 'Minimal')],
                    default='modern', max_length=20)),
                ('full_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('linkedin', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('summary', models.TextField(blank=True)),
                ('experience', models.TextField(blank=True, default='[]')),
                ('education', models.TextField(blank=True, default='[]')),
                ('skills', models.TextField(blank=True)),
                ('projects', models.TextField(blank=True, default='[]')),
                ('certifications', models.TextField(blank=True)),
                ('ai_enhanced', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='built_resumes',
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]