from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Job, Application
from .forms import JobForm, ApplicationForm
from resumes.models import Resume
from resumes.utils import calculate_match_score

def home(request):
    jobs = Job.objects.filter(is_active=True).order_by('-created_at')[:6]
    total_jobs = Job.objects.filter(is_active=True).count()
    return render(request, 'jobs/home.html', {'jobs': jobs, 'total_jobs': total_jobs})

def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    q = request.GET.get('q', '')
    location = request.GET.get('location', '')
    job_type = request.GET.get('job_type', '')
    level = request.GET.get('level', '')
    if q:
        jobs = jobs.filter(Q(title__icontains=q) | Q(company__icontains=q) | Q(skills_required__icontains=q))
    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if level:
        jobs = jobs.filter(level=level)
    return render(request, 'jobs/job_list.html', {
        'jobs': jobs.order_by('-created_at'),
        'q': q, 'location': location, 'job_type': job_type, 'level': level,
    })

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    has_applied = False
    if request.user.is_authenticated:
        has_applied = Application.objects.filter(job=job, applicant=request.user).exists()
    return render(request, 'jobs/job_detail.html', {'job': job, 'has_applied': has_applied})

@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if not request.user.is_seeker():
        messages.error(request, 'Only job seekers can apply.')
        return redirect('job_detail', pk=pk)
    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, 'You have already applied to this job.')
        return redirect('job_detail', pk=pk)
    resumes = Resume.objects.filter(user=request.user)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        resume_id = request.POST.get('resume_id')
        resume = Resume.objects.filter(pk=resume_id, user=request.user).first()
        if form.is_valid():
            app = form.save(commit=False)
            app.job = job
            app.applicant = request.user
            app.resume = resume
            if resume:
                app.match_score = calculate_match_score(resume, job)
            app.save()
            messages.success(request, f'Applied to {job.title} successfully!')
            return redirect('dashboard')
    else:
        form = ApplicationForm()
    return render(request, 'jobs/apply.html', {'job': job, 'form': form, 'resumes': resumes})

@login_required
def post_job(request):
    if not request.user.is_recruiter():
        messages.error(request, 'Only recruiters can post jobs.')
        return redirect('home')
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('dashboard')
    else:
        form = JobForm(initial={'company': request.user.company})
    return render(request, 'jobs/post_job.html', {'form': form})

@login_required
def edit_job(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated!')
            return redirect('dashboard')
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/post_job.html', {'form': form, 'edit': True})

@login_required
def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted.')
    return redirect('dashboard')

@login_required
def view_applications(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)
    applications = job.applications.all().order_by('-match_score')
    return render(request, 'jobs/applications.html', {'job': job, 'applications': applications})

@login_required
def update_application_status(request, pk):
    app = get_object_or_404(Application, pk=pk, job__recruiter=request.user)
    status = request.POST.get('status')
    if status in dict(Application.STATUS_CHOICES):
        app.status = status
        app.save()
        messages.success(request, f'Application status updated to {status}.')
    return redirect('view_applications', pk=app.job.pk)
