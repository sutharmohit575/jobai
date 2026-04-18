"""
Run this from your project root (same folder as manage.py):

    python load_demo_data.py

Creates demo users + 12 real Indian tech company jobs.
Safe to run multiple times — won't create duplicates.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobai.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from accounts.models import User
from jobs.models import Job

# ── USERS ──────────────────────────────────────────────────────────────────

# recruiter, created = User.objects.get_or_create(
#     username='demo_recruiter',
#     defaults={
#         'email': 'recruiter@jobai.demo',
#         'first_name': 'Priya',
#         'last_name': 'Mehta',
#         'role': 'recruiter',
#         'company': 'JobAI Demo',
#         'location': 'Bangalore',
#         'password': make_password('demo1234'),
#     }
# )
# print(f"{'Created' if created else 'Found'} recruiter → demo_recruiter / demo1234")

# seeker, created = User.objects.get_or_create(
#     username='demo_seeker',
#     defaults={
#         'email': 'seeker@jobai.demo',
#         'first_name': 'Arjun',
#         'last_name': 'Sharma',
#         'role': 'seeker',
#         'location': 'Bangalore',
#         'bio': 'Full Stack Developer with 4 years of experience in Python, Django, and React.',
#         'password': make_password('demo1234'),
#     }
# )
# print(f"{'Created' if created else 'Found'} seeker    → demo_seeker / demo1234")

# ── JOBS ───────────────────────────────────────────────────────────────────

JOBS = [
    dict(
        title='Senior Full Stack Developer', company='Infosys Digital',
        location='Bangalore, Karnataka', job_type='full-time', level='senior',
        skills_required='Python, Django, React, TypeScript, PostgreSQL, Docker, AWS, REST API, Git',
        salary_min=1800000, salary_max=3000000,
        description='Build scalable full-stack applications serving millions of users across India. Work with Python/Django backend and React/TypeScript frontend deployed on AWS.',
        requirements='5+ years Python/Django, Advanced React+TypeScript, PostgreSQL optimization, AWS services, Docker/Kubernetes, Bachelor\'s in CS or equivalent.',
    ),
    dict(
        title='Machine Learning Engineer', company='Flipkart AI Labs',
        location='Bangalore, Karnataka', job_type='full-time', level='mid',
        skills_required='Python, Machine Learning, TensorFlow, PyTorch, Scikit-learn, SQL, Docker, MLOps, Pandas, NumPy',
        salary_min=2000000, salary_max=3500000,
        description='Build and deploy ML models for recommendations, fraud detection, and demand forecasting at Flipkart scale. Own the full ML lifecycle from data exploration to production monitoring.',
        requirements='3+ years ML engineering, TensorFlow or PyTorch, MLOps tools, SQL proficiency, large-scale data systems experience, MS/PhD preferred.',
    ),
    dict(
        title='React Native Mobile Developer', company='CRED',
        location='Bangalore, Karnataka', job_type='full-time', level='mid',
        skills_required='React Native, JavaScript, TypeScript, Redux, REST API, iOS, Android, Git, Jest',
        salary_min=1400000, salary_max=2400000,
        description='Build pixel-perfect mobile experiences for CRED\'s 12 million members. Work with a world-class design team on performance-first React Native features.',
        requirements='3+ years React Native, strong TypeScript, Redux/MobX state management, mobile performance optimization, eye for design detail.',
    ),
    dict(
        title='DevOps / Cloud Engineer', company='Razorpay',
        location='Bangalore, Karnataka', job_type='full-time', level='senior',
        skills_required='AWS, Kubernetes, Terraform, Docker, Linux, Python, CI/CD, Jenkins, Prometheus, Grafana',
        salary_min=2200000, salary_max=3800000,
        description='Own critical cloud infrastructure at Razorpay — high availability, disaster recovery, and security hardening across our AWS multi-region setup.',
        requirements='5+ years DevOps/SRE, expert AWS, Kubernetes administration, Terraform IaC, Python/Bash scripting, Prometheus+Grafana monitoring.',
    ),
    dict(
        title='Data Analyst', company='Swiggy',
        location='Bangalore, Karnataka', job_type='full-time', level='entry',
        skills_required='SQL, Python, Data Analysis, Pandas, Tableau, Excel, Statistics, Communication',
        salary_min=700000, salary_max=1200000,
        description='Turn millions of daily orders into insights for Swiggy\'s Growth Analytics team. Measure A/B experiments and surface actionable data for PMs and marketers.',
        requirements='0-2 years data analysis, strong SQL, Python Pandas, Tableau or similar BI tool, statistics fundamentals, quantitative degree.',
    ),
    dict(
        title='UI/UX Designer', company='Meesho',
        location='Bangalore, Karnataka', job_type='full-time', level='mid',
        skills_required='Figma, UX Design, UI Design, Prototyping, User Research, Design Systems, CSS, Communication',
        salary_min=1200000, salary_max=2000000,
        description='Design experiences for Bharat — users who may be using smartphones for the first time. Own design end-to-end from user research to engineering handoff.',
        requirements='3+ years UI/UX design, expert Figma, design systems experience, portfolio showing full design process, basic HTML/CSS.',
    ),
    dict(
        title='Backend Engineer — Node.js', company='PhonePe',
        location='Bangalore, Karnataka', job_type='full-time', level='mid',
        skills_required='Node.js, JavaScript, TypeScript, PostgreSQL, Redis, REST API, Microservices, Docker, AWS',
        salary_min=1600000, salary_max=2800000,
        description='Build high-throughput Node.js microservices for real-time payment processing at PhonePe — 5 billion transactions per year.',
        requirements='3+ years Node.js, strong TypeScript, PostgreSQL optimization, Redis caching, RESTful APIs at scale, Docker, distributed systems knowledge.',
    ),
    dict(
        title='Python Django Developer', company='Zoho Corporation',
        location='Chennai, Tamil Nadu', job_type='full-time', level='entry',
        skills_required='Python, Django, REST API, SQL, HTML, CSS, JavaScript, Git',
        salary_min=600000, salary_max=1000000,
        description='Build features for Zoho\'s business apps used by 55 million users worldwide. Great opportunity for entry-level developers to work on real products at scale.',
        requirements='0-2 years Django experience, Django ORM, REST APIs, basic HTML/CSS/JavaScript, Git, BE/BTech CS or IT.',
    ),
    dict(
        title='Cybersecurity Analyst', company='HCL Technologies',
        location='Noida, Uttar Pradesh', job_type='full-time', level='mid',
        skills_required='Cybersecurity, Network Security, SIEM, Penetration Testing, Linux, Python, Incident Response, Firewall',
        salary_min=1000000, salary_max=1800000,
        description='Monitor, investigate, and respond to security threats for Fortune 500 clients in HCL\'s 24/7 Security Operations Center.',
        requirements='3+ years SOC/cybersecurity, SIEM tools, penetration testing skills, Linux command line, Python scripting, OSCP/CEH/Security+ preferred.',
    ),
    dict(
        title='Frontend Developer Intern', company='Freshworks',
        location='Chennai, Tamil Nadu', job_type='internship', level='entry',
        skills_required='HTML, CSS, JavaScript, React, Git, Communication, Problem Solving',
        salary_min=25000, salary_max=40000,
        description='Real internship — ship features to production for Freshdesk or Freshsales used by 60,000+ businesses. Build React components and contribute to the component library.',
        requirements='Pursuing or completed BTech/BE CS/IT/ECE, solid HTML/CSS/JS, basic React, Git, GitHub portfolio with 2+ projects, available full-time 6 months.',
    ),
    dict(
        title='Product Manager — Consumer App', company='Ola',
        location='Bangalore, Karnataka', job_type='full-time', level='senior',
        skills_required='Product Management, Data Analysis, SQL, Communication, Leadership, Agile, User Research, Roadmap Planning',
        salary_min=2500000, salary_max=4500000,
        description='Own a key product area for the Ola app used by tens of millions of riders across India — driver supply, pricing, or rider experience.',
        requirements='5+ years PM experience, consumer apps at scale, strong SQL and A/B testing, excellent communication, track record of shipping high-impact products.',
    ),
    dict(
        title='Cloud Solutions Architect', company='Wipro',
        location='Hyderabad, Telangana', job_type='full-time', level='lead',
        skills_required='AWS, Azure, Cloud Architecture, Terraform, Kubernetes, Docker, Python, Microservices, Security, Leadership',
        salary_min=3000000, salary_max=5000000,
        description='Lead cloud architecture for major enterprise transformation engagements at Wipro. Design AWS and Azure solutions for Fortune 500 companies worldwide.',
        requirements='8+ years IT / 4+ years cloud architecture, AWS Professional or Azure Expert certified, Terraform, Kubernetes, excellent client presentation skills.',
    ),
]

if Job.objects.count() > 0:
    print(f"\nFound {Job.objects.count()} existing jobs. Deleting and recreating...")
    Job.objects.all().delete()

for job in JOBS:
    Job.objects.create(recruiter=recruiter, **job)

print(f"\n✓ {Job.objects.count()} jobs created successfully!")
# print("\n─────────────────────────────────────")
# print("  Demo Accounts:")
# print("  Seeker    → demo_seeker / demo1234")
# print("  Recruiter → demo_recruiter / demo1234")
# print("─────────────────────────────────────")
# print("\nNow upload 'demo_resume_arjun_sharma.txt' as demo_seeker to test AI analysis.")
