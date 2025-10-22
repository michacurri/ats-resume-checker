# Technical Context: AI Resume Checker

## Technology Stack

### Frontend Technologies
- **React 19.1.1**: Latest React with concurrent features
- **TypeScript 5.9.3**: Type safety and better developer experience
- **Vite 7.1.7**: Fast build tool and development server
- **React Router DOM 7.9.4**: Client-side routing
- **TanStack React Query 5.90.5**: Server state management and caching
- **Axios 1.12.2**: HTTP client for API communication

### Backend Technologies
- **Django 4.2.25**: Web framework with built-in admin and ORM
- **Django REST Framework 3.15.2**: API development framework
- **Python 3.x**: Core programming language
- **SQLite**: Development database (lightweight, file-based)

### File Processing Libraries
- **PyMuPDF 1.24.11**: PDF text extraction and manipulation
- **python-docx 1.1.2**: Microsoft Word document processing
- **BeautifulSoup4 4.14.2**: HTML/XML parsing for complex documents
- **lxml 6.0.2**: XML processing library

### Development Tools
- **ESLint**: Code linting and formatting
- **TypeScript ESLint**: TypeScript-specific linting rules
- **Docker**: Containerization for consistent environments
- **Git**: Version control

## Development Environment

### Prerequisites
- Node.js 18+ (for frontend development)
- Python 3.8+ (for backend development)
- Docker & Docker Compose (for containerized development)
- Git (for version control)

### Project Structure
```
ai-resume-checker/
├── frontend/                 # React TypeScript application
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/           # Page components
│   │   ├── hooks/           # Custom React hooks
│   │   ├── services/        # API service functions
│   │   └── types/           # TypeScript type definitions
│   ├── package.json
│   └── vite.config.ts
├── backend/                  # Django application
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── resume_api/              # Django app for resume processing
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── utils/
├── memory-bank/             # Project documentation
├── docker-compose.yml
├── requirements.txt
└── manage.py
```

### Development Setup
1. **Backend**: Django development server on port 8000
2. **Frontend**: Vite development server on port 5173
3. **Database**: SQLite file (`db.sqlite3`)
4. **File Storage**: Local filesystem (development)

## API Endpoints (Planned)
- `POST /api/resumes/upload/` - Upload resume file
- `GET /api/resumes/` - List user resumes
- `GET /api/resumes/{id}/` - Get resume details
- `POST /api/resumes/{id}/analyze/` - Trigger analysis
- `GET /api/resumes/{id}/analysis/` - Get analysis results
- `GET /api/resumes/{id}/recommendations/` - Get improvement suggestions

## Database Schema (Planned)
```python
# Resume model
class Resume(models.Model):
    id = models.UUIDField(primary_key=True)
    filename = models.CharField(max_length=255)
    file_path = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=10)

# Analysis model
class Analysis(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)
    raw_text = models.TextField()
    ats_score = models.IntegerField()
    keyword_score = models.IntegerField()
    format_score = models.IntegerField()
    overall_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

# Recommendation model
class Recommendation(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)  # 'ats', 'keywords', 'format'
    priority = models.CharField(max_length=10)   # 'high', 'medium', 'low'
    suggestion = models.TextField()
    confidence = models.FloatField()
```

## Configuration Management
- **Environment Variables**: Separate configs for development/production
- **Django Settings**: Modular settings with environment-specific overrides
- **Frontend Config**: Vite environment variables for API endpoints
- **Docker**: Environment-specific docker-compose files

## Dependencies Management
- **Python**: `requirements.txt` with pinned versions
- **Node.js**: `package.json` with semantic versioning
- **Docker**: Multi-stage builds for optimized images
- **Security**: Regular dependency updates and vulnerability scanning

## Performance Considerations
- **File Size Limits**: Configurable upload limits (default 10MB)
- **Processing Timeouts**: Async processing with progress tracking
- **Database Queries**: Optimized queries with proper indexing
- **Frontend Bundle**: Code splitting and lazy loading
- **Caching**: Redis for production (future enhancement)

## Security Measures
- **File Validation**: Strict file type checking and virus scanning (future)
- **Input Sanitization**: All user inputs cleaned and validated
- **CORS**: Proper cross-origin resource sharing configuration
- **Rate Limiting**: API rate limiting to prevent abuse (future)
- **Authentication**: JWT tokens for user sessions (future)
