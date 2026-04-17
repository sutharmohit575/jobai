from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Resume
from .forms import ResumeUploadForm
from .utils import extract_text_from_file, extract_skills, estimate_experience, generate_ai_analysis
import os

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            # Extract text
            file_path = resume.file.path
            raw_text = extract_text_from_file(file_path)
            resume.raw_text = raw_text
            resume.skills = extract_skills(raw_text)
            resume.experience_years = estimate_experience(raw_text)
            summary, score, suggestions = generate_ai_analysis(resume)
            resume.ai_summary = summary
            resume.ai_score = score
            resume.ai_suggestions = suggestions
            resume.analyzed = True
            resume.save()
            messages.success(request, 'Resume uploaded and analyzed by AI!')
            return redirect('resume_detail', pk=resume.pk)
    else:
        form = ResumeUploadForm()
    return render(request, 'resumes/upload.html', {'form': form})

@login_required
def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    return render(request, 'resumes/detail.html', {'resume': resume})

@login_required
def delete_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if request.method == 'POST':
        if os.path.exists(resume.file.path):
            os.remove(resume.file.path)
        resume.delete()
        messages.success(request, 'Resume deleted.')
    return redirect('dashboard')

@login_required
def reanalyze_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    raw_text = extract_text_from_file(resume.file.path)
    resume.raw_text = raw_text
    resume.skills = extract_skills(raw_text)
    resume.experience_years = estimate_experience(raw_text)
    summary, score, suggestions = generate_ai_analysis(resume)
    resume.ai_summary = summary
    resume.ai_score = score
    resume.ai_suggestions = suggestions
    resume.analyzed = True
    resume.save()
    messages.success(request, 'Resume re-analyzed!')
    return redirect('resume_detail', pk=pk)
