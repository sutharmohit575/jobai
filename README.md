# JobAI — AI-Powered Job Portal

A full-featured Django web application with AI resume analysis and intelligent job matching.

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run migrations
python manage.py migrate

# 3. Start server
python manage.py runserver
```

Open http://127.0.0.1:8000

## 👤 Demo Accounts

| Role | Username | Password |
|------|----------|----------|
| Job Seeker | demo_seeker | demo1234 |
| Recruiter | demo_recruiter | demo1234 |
| Admin | admin | admin123 |

## 📁 Project Structure

```
jobai/
├── accounts/       # User auth (seeker + recruiter roles)
├── jobs/           # Job postings + applications
├── resumes/        # AI resume analysis engine
├── templates/      # All HTML templates
├── static/         # CSS, JS assets
└── media/          # Uploaded resume files
```

## ✨ Features

### Job Seekers
- Signup/Login with role selection
- Upload resume (PDF, DOCX, TXT)
- AI analysis: skill extraction, score (0–100), suggestions
- Browse & filter jobs
- One-click apply with resume + cover letter
- AI match score per job application
- Track application status in dashboard

### Recruiters
- Post & manage job listings
- View applicants ranked by AI match score
- Update application status (pending/reviewing/accepted/rejected)
- Download applicant resumes

### AI Engine (resumes/utils.py)
- Extracts 30+ common tech/soft skills
- Estimates experience from text patterns
- Scores resume quality (0–100)
- Generates improvement suggestions
- Calculates job-resume match %

## 🛠 Tech Stack
- Python 3.11+, Django 4.2
- SQLite (dev) — swap to PostgreSQL for production
- Vanilla JS + CSS (no frontend framework needed)
- Google Fonts: Syne + DM Sans
