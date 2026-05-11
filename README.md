# 🚀 JobAI — AI-Powered Job Portal

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.x-green)](https://djangoproject.com)
[![Deployment](https://img.shields.io/badge/Deployed-Vercel-black)](https://vercel.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

🌐 **Live Demo:**
👉 [![Live Demo](https://img.shields.io/badge/Live%20Demo-View%20Project-brightgreen?style=for-the-badge)](https://jobai-sutharmohit575.vercel.app)

---

## 📌 Overview

**JobAI** is a modern AI-powered job portal built with Django.
It allows users to explore jobs, apply easily, and manage resumes while providing admins with a powerful dashboard to manage the platform.

---

## ✨ Features

### 👤 User Features

- 🔐 User authentication (Login / Register)
- 📄 Resume upload & management
- 💼 Browse and apply for jobs
- 📊 Personalized dashboard

### 🧑‍💼 Admin Features

- 🛠️ Django Admin Panel (custom UI)
- 👥 Manage users
- 📋 Manage job listings
- 📑 Track applications

### ⚙️ Technical Features

- ⚡ Django-based backend
- 🎨 Custom admin UI (styled)
- 🌐 Deployed on Vercel
- 🗄️ PostgreSQL database (production)
- 🔒 CSRF & security configured

---

## 🏗️ Tech Stack

| Technology | Usage |
| --- | --- |
| Python | Backend |
| Django | Web Framework |
| PostgreSQL | Database (Production) |
| SQLite | Local Development |
| HTML/CSS | Frontend |
| Vercel | Deployment |

---

## 📁 Project Structure

```
JobAI/
│
├── accounts/        # User authentication app
├── jobs/            # Job management
├── resumes/         # Resume handling
├── templates/       # HTML templates
├── static/          # CSS, JS, images
├── jobai/           # Main project settings
├── manage.py
└── db.sqlite3       # Local database
```

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/sutharmohit575/jobai.git
cd jobai
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

👉 Open: http://127.0.0.1:8000/

---

## 🌍 Deployment (Vercel)

### Steps:

1. Push code to GitHub
2. Go to [vercel.com](https://vercel.com) → New Project → Import your repo
3. Add environment variables:

```
SECRET_KEY=your_secret_key
DEBUG=False
DATABASE_URL=your_postgres_url
```

4. Click **Deploy** 🚀

> Vercel auto-detects the project. Make sure you have a `vercel.json` or `wsgi` entry point configured for Django.

---

## 🔐 Environment Variables

| Variable | Description |
| --- | --- |
| SECRET_KEY | Django secret key |
| DEBUG | Set False in production |
| DATABASE_URL | PostgreSQL connection string |

---

## 🛡️ Security Notes

- CSRF protection enabled
- Secure cookies configured
- Environment variables used for secrets

---

## 🧠 Future Improvements

- 🤖 AI Resume Analyzer
- 📊 Job recommendation system
- 💬 Chatbot integration
- 📈 Analytics dashboard

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a branch
3. Make changes
4. Submit PR

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Mohit Suthar**
- GitHub: [sutharmohit575](https://github.com/sutharmohit575)
- LinkedIn: [sutharmohit575](https://linkedin.com/in/sutharmohit575)

---

## ⭐ Support

If you like this project, please ⭐ the repo and share it!
