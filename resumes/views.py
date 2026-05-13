from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Resume, ResumeBuilder
from .forms import ResumeUploadForm
from .utils import extract_text_from_file, extract_skills, estimate_experience, generate_ai_analysis
import os, json

# ── UPLOAD VIEWS ──────────────────────────────────────────────────────────────

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            raw_text = extract_text_from_file(resume.file.url)
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
        resume.delete()
        messages.success(request, 'Resume deleted.')
    return redirect('dashboard')

@login_required
def reanalyze_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    raw_text = extract_text_from_file(resume.file.url)
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

# ── BUILDER VIEWS ─────────────────────────────────────────────────────────────

def _safe_json(val, default):
    try:
        return json.loads(val) if val else default
    except Exception:
        return default

@login_required
def builder_list(request):
    resumes = ResumeBuilder.objects.filter(user=request.user).order_by('-updated_at')
    return render(request, 'resumes/builder_list.html', {'resumes': resumes})

@login_required
def builder_create(request):
    user = request.user
    resume = ResumeBuilder.objects.create(
        user=user, title='My Resume',
        full_name=user.get_full_name() or user.username,
        email=user.email,
        phone=getattr(user, 'phone', ''),
        location=getattr(user, 'location', ''),
        experience='[]', education='[]', projects='[]',
    )
    return redirect('builder_edit', pk=resume.pk)

@login_required
def builder_edit(request, pk):
    resume = get_object_or_404(ResumeBuilder, pk=pk, user=request.user)
    context = {
        'resume': resume,
        'experience_json': json.dumps(_safe_json(resume.experience, [])),
        'education_json':  json.dumps(_safe_json(resume.education, [])),
        'projects_json':   json.dumps(_safe_json(resume.projects, [])),
    }
    return render(request, 'resumes/builder_edit.html', context)

@login_required
def builder_save(request, pk):
    resume = get_object_or_404(ResumeBuilder, pk=pk, user=request.user)
    if request.method == 'POST':
        resume.title          = request.POST.get('title', 'My Resume')
        resume.template       = request.POST.get('template', 'modern')
        resume.full_name      = request.POST.get('full_name', '')
        resume.email          = request.POST.get('email', '')
        resume.phone          = request.POST.get('phone', '')
        resume.location       = request.POST.get('location', '')
        resume.linkedin       = request.POST.get('linkedin', '')
        resume.github         = request.POST.get('github', '')
        resume.website        = request.POST.get('website', '')
        resume.summary        = request.POST.get('summary', '')
        resume.skills         = request.POST.get('skills', '')
        resume.certifications = request.POST.get('certifications', '')
        resume.experience     = request.POST.get('experience_json', '[]')
        resume.education      = request.POST.get('education_json', '[]')
        resume.projects       = request.POST.get('projects_json', '[]')
        resume.save()
        messages.success(request, 'Resume saved successfully!')
    return redirect('builder_edit', pk=pk)

@login_required
def builder_ai_enhance(request, pk):
    resume = get_object_or_404(ResumeBuilder, pk=pk, user=request.user)
    if request.method == 'POST':
        section  = request.POST.get('section', 'summary')
        content  = request.POST.get('content', '')
        job_role = request.POST.get('job_role', 'Software Developer')
        result   = _ai_enhance(section, content, job_role, resume)
        return HttpResponse(result, content_type='text/plain')
    return HttpResponse('', status=400)

@login_required
def builder_preview(request, pk):
    resume = get_object_or_404(ResumeBuilder, pk=pk, user=request.user)
    context = {
        'resume': resume,
        'experience':   _safe_json(resume.experience, []),
        'education':    _safe_json(resume.education, []),
        'projects':     _safe_json(resume.projects, []),
        'skills_list':  [s.strip() for s in resume.skills.split(',') if s.strip()],
        'certs_list':   [c.strip() for c in resume.certifications.split('\n') if c.strip()],
    }
    return render(request, 'resumes/builder_preview.html', context)

@login_required
def builder_delete(request, pk):
    resume = get_object_or_404(ResumeBuilder, pk=pk, user=request.user)
    if request.method == 'POST':
        resume.delete()
        messages.success(request, 'Resume deleted.')
    return redirect('builder_list')

# ── AI ENGINE ─────────────────────────────────────────────────────────────────

def _ai_enhance(section, content, job_role, resume):
    if section == 'summary':
        skills = resume.skills[:120] if resume.skills else 'modern technologies'
        if content.strip():
            return (f"Results-driven {job_role} with expertise in {skills}. "
                    f"Proven track record of delivering scalable solutions and driving measurable business impact. "
                    f"Strong communicator with experience in cross-functional teams and Agile environments. "
                    f"Passionate about clean code, performance optimization, and continuous learning.")
        return (f"Motivated {job_role} with a solid foundation in software development and a passion for building "
                f"impactful digital products. Experienced with modern tech stacks and collaborative team environments. "
                f"Eager to bring technical skills and fresh perspective to challenging real-world problems.")

    elif section == 'experience_bullet':
        verbs = ['Architected', 'Engineered', 'Spearheaded', 'Optimized', 'Delivered', 'Streamlined']
        if content.strip():
            lines = [l.strip('•- ').strip() for l in content.split('\n') if l.strip()]
            enhanced = []
            for i, line in enumerate(lines[:5]):
                if not any(c.isdigit() for c in line):
                    line = line.rstrip('.') + f', improving efficiency by {(i+2)*10}%'
                enhanced.append(f"• {verbs[i % len(verbs)]} {line[0].lower()}{line[1:]}")
            return '\n'.join(enhanced)
        return '\n'.join([
            f"• Designed and built scalable {job_role.lower()} features serving 100K+ users, boosting performance by 35%",
            f"• Led end-to-end delivery of 3 major product releases, collaborating with design and product teams",
            f"• Reduced deployment time by 50% by implementing Docker-based CI/CD pipelines",
            f"• Mentored 2 junior developers through weekly code reviews and pair programming",
        ])

    elif section == 'project':
        return (f"Built a production-ready {job_role.lower()} platform with React frontend and Django REST API. "
                f"Implemented JWT authentication, real-time updates, and deployed on AWS with Docker. "
                f"Achieved 99.9% uptime with Redis caching reducing load time by 60%. "
                f"Stack: Python, Django, React, PostgreSQL, Redis, Docker, AWS.")

    elif section == 'skills':
        presets = {
            'data':     'Python, Machine Learning, TensorFlow, Pandas, NumPy, SQL, Tableau, Scikit-learn, Power BI',
            'devops':   'AWS, Docker, Kubernetes, Terraform, Linux, Python, CI/CD, Jenkins, Prometheus, Grafana',
            'frontend': 'JavaScript, TypeScript, React, Vue.js, HTML5, CSS3, Tailwind, Redux, Jest, Figma',
            'mobile':   'React Native, Flutter, JavaScript, TypeScript, Redux, iOS, Android, Firebase, REST API',
            'default':  'Python, Django, React, TypeScript, PostgreSQL, Docker, AWS, Git, REST API, Redis',
        }
        r = job_role.lower()
        key = 'data' if any(x in r for x in ['data','ml','analyst']) else \
              'devops' if any(x in r for x in ['devops','cloud','infra']) else \
              'frontend' if any(x in r for x in ['frontend','ui','ux']) else \
              'mobile' if any(x in r for x in ['mobile','android','ios']) else 'default'
        return presets[key]

    return content