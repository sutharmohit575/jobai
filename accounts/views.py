from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, LoginForm, ProfileForm
from jobs.models import Job, Application
from resumes.models import Resume

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to JobAI, {user.first_name}!')
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    user = request.user
    if user.is_recruiter():
        jobs = Job.objects.filter(recruiter=user).order_by('-created_at')
        total_applications = Application.objects.filter(job__recruiter=user).count()
        recent_apps = Application.objects.filter(job__recruiter=user).order_by('-applied_at')[:5]
        context = {
            'jobs': jobs,
            'total_applications': total_applications,
            'recent_apps': recent_apps,
            'total_jobs': jobs.count(),
        }
    else:
        applications = Application.objects.filter(applicant=user).order_by('-applied_at')
        resumes = Resume.objects.filter(user=user).order_by('-uploaded_at')
        context = {
            'applications': applications,
            'resumes': resumes,
            'total_applications': applications.count(),
            'pending': applications.filter(status='pending').count(),
            'accepted': applications.filter(status='accepted').count(),
        }
    return render(request, 'accounts/dashboard.html', context)

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})
