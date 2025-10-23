### A POC Application to help me learn Django / Python
I am using this idea to showcase my understanding of building tools with a React (TS) frontend, and an LLM-integrated backend.
As someone who is proficient with JS/TS and works with NodeJS in production environments, I decided to step outside of my boundaries and build this as a full-stack Django + Vite application.

Obviously I am using AI to help scaffold this, but I am using it only to support my learning, and as I go making detailed notes and asking AI questions on each decision that is made.

Below is the concept that is being built here:

# AI Resume Checker & Career Coach

An AI-powered resume analysis platform that helps job seekers optimize their resumes for better job matching, ATS compatibility, and career growth. The platform analyzes resumes against job descriptions and provides personalized feedback, interview prep guidance, and career trajectory insights.

## 🚀 Features

### Core Functionality
- **Resume Upload & Processing**: Support for PDF, DOCX, and TXT formats
- **AI-Powered Analysis**: LLM-based resume evaluation with ATS and match scoring
- **Job Description Integration**: Web scraping and manual entry of job descriptions
- **Personalized Feedback**: Industry-specific recommendations and skill gap analysis
- **Career Coaching**: Interview prep guidance and career trajectory insights

### Advanced Features
- **User Job Interest Tracking**: Track which jobs users are interested in for personalization
- **Shared Job Database**: Efficient storage by sharing job descriptions across users
- **Evaluation Caching**: Cache AI evaluations by prompt hash for performance
- **Single Active Resume**: MVP enforces one active resume per user (growth-ready schema)

## Architecture

### Tech Stack
- **Frontend**: React 19 + TypeScript + Vite
- **Backend**: Django 4.2 + Django REST Framework
- **Database**: PostgreSQL
- **AI Integration**: OpenAI/Anthropic LLM APIs
- **File Processing**: PyMuPDF, python-docx, BeautifulSoup4

### Project Structure
```
ai-resume-checker/
├── frontend/                # React + TypeScript frontend
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
├── backend/                 # Django backend
│   ├── resume_api/          # Main Django app
│   │   ├── models.py        # Database models
│   │   ├── views.py         # API ViewSets
│   │   ├── serializers.py   # DRF serializers
│   │   └── urls.py          # API routing
│   ├── settings.py
│   └── urls.py
├── memory-bank/             # Project documentation for agentic support (similar to Cline)
├── docker-compose.yml
└── requirements.txt
```

## 📊 Database Schema

### Models
- **Resume**: User resumes with text extraction and SHA-256 hashing
- **JobDescription**: Shared job descriptions with URL and content deduplication
- **UserJobInterest**: Many-to-many tracking of user interest in jobs
- **Evaluation**: AI evaluation results with caching and token tracking

### Key Relationships
- User → Resumes (one-to-many, single active)
- User → JobInterest → JobDescription (many-to-many)
- Resume + JobDescription → Evaluation (analysis results)

---

**Built with ❤️ for job seekers everywhere**
