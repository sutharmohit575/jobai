import re
import os

COMMON_SKILLS = [
    'python', 'javascript', 'java', 'c++', 'react', 'django', 'flask',
    'node.js', 'sql', 'postgresql', 'mysql', 'mongodb', 'redis',
    'docker', 'kubernetes', 'aws', 'azure', 'gcp', 'git', 'linux',
    'machine learning', 'deep learning', 'tensorflow', 'pytorch',
    'data analysis', 'pandas', 'numpy', 'scikit-learn',
    'html', 'css', 'typescript', 'vue', 'angular', 'spring',
    'rest api', 'graphql', 'microservices', 'agile', 'scrum',
    'communication', 'leadership', 'problem solving', 'teamwork',
]

import requests
import io

def extract_text_from_file(file_path_or_url):
    try:
        # Handle Cloudinary URLs or any remote file URL
        if file_path_or_url.startswith('http'):
            response = requests.get(file_path_or_url)
            file_bytes = io.BytesIO(response.content)
            import pdfplumber
            with pdfplumber.open(file_bytes) as pdf:
                return '\n'.join(page.extract_text() or '' for page in pdf.pages)
        else:
            with open(file_path_or_url, 'rb') as f:
                content = f.read()
            text = content.decode('utf-8', errors='ignore')
            text = re.sub(r'[^\x20-\x7E\n\r\t]', ' ', text)
            text = re.sub(r'\s+', ' ', text)
            return text[:5000]
    except Exception:
        return ""

def extract_skills(text):
    """Extract skills from resume text."""
    text_lower = text.lower()
    found = []
    for skill in COMMON_SKILLS:
        if skill in text_lower:
            found.append(skill.title())
    return ', '.join(found) if found else 'Python, Communication, Problem Solving'

def estimate_experience(text):
    """Estimate years of experience from text."""
    patterns = [
        r'(\d+)\+?\s*years?\s+of\s+experience',
        r'experience[:\s]+(\d+)\+?\s*years?',
        r'(\d{4})\s*[-–]\s*(?:present|current|now)',
    ]
    for pattern in patterns:
        matches = re.findall(pattern, text.lower())
        if matches:
            val = int(matches[0])
            if val > 1900:  # It's a year
                import datetime
                return min(datetime.datetime.now().year - val, 30)
            return min(val, 30)
    return 0

def generate_ai_analysis(resume):
    """Simulate AI analysis of resume."""
    text = resume.raw_text or ""
    skills = resume.get_skills_list()
    skill_count = len(skills)
    has_education = any(w in text.lower() for w in ['bachelor', 'master', 'phd', 'degree', 'university', 'college'])
    has_projects = any(w in text.lower() for w in ['project', 'built', 'developed', 'created'])
    
    score = 50
    if skill_count > 5: score += 15
    if skill_count > 10: score += 10
    if has_education: score += 15
    if has_projects: score += 10
    if resume.experience_years > 0: score += min(resume.experience_years * 2, 10)
    score = min(score, 98)

    summary = f"This resume showcases a professional with {resume.experience_years:.0f}+ years of experience. "
    summary += f"Key technical skills include {', '.join(skills[:5]) if skills else 'various skills'}. "
    if has_education:
        summary += "The candidate demonstrates solid educational background. "
    if has_projects:
        summary += "Hands-on project experience is evident."

    suggestions = []
    if skill_count < 5:
        suggestions.append("Add more specific technical skills relevant to your target role.")
    if not has_projects:
        suggestions.append("Include project descriptions with measurable outcomes.")
    if resume.experience_years == 0:
        suggestions.append("Clearly state your total years of experience.")
    if not has_education:
        suggestions.append("Add your educational qualifications section.")
    if len(text) < 300:
        suggestions.append("Expand your resume with more detailed descriptions of your work.")
    if not suggestions:
        suggestions.append("Great resume! Consider tailoring keywords for specific job descriptions.")
        suggestions.append("Add quantifiable achievements (e.g., 'Increased performance by 40%').")

    return summary, score, '\n'.join(f"• {s}" for s in suggestions)

def calculate_match_score(resume, job):
    """Calculate match score between resume and job."""
    resume_skills = set(s.lower() for s in resume.get_skills_list())
    job_skills = set(s.lower() for s in job.get_skills_list())
    if not job_skills:
        return 50.0
    matched = resume_skills.intersection(job_skills)
    base_score = (len(matched) / len(job_skills)) * 100 if job_skills else 50
    # Bonus for experience
    if resume.experience_years > 0:
        base_score = min(base_score + 5, 100)
    return round(base_score, 1)
