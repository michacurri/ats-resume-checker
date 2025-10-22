# System Patterns: AI Resume Checker

## Architecture Overview
```
Frontend (React/TypeScript) ←→ Backend (Django REST) ←→ Database (SQLite/PostgreSQL)
                ↓
        File Processing Pipeline
                ↓
        AI Analysis Engine
```

## Core Components

### Frontend Architecture
- **Framework**: React 19 with TypeScript
- **Build Tool**: Vite for fast development and building
- **State Management**: React Query (@tanstack/react-query) for server state
- **Routing**: React Router DOM for navigation
- **HTTP Client**: Axios for API communication
- **Styling**: CSS modules or styled-components (TBD)

### Backend Architecture
- **Framework**: Django 4.2 with Django REST Framework
- **API Design**: RESTful endpoints with JSON responses, custom @action decorators
- **File Processing**: Multi-format support (PDF, DOCX, TXT)
- **Database**: SQLite for development, PostgreSQL for production
- **Authentication**: Django's built-in auth system with IsAuthenticated permissions
- **User Isolation**: get_queryset() pattern for row-level security
- **Business Logic**: perform_create() for model creation with custom logic

### File Processing Pipeline
1. **Upload Handler**: Receive and validate file uploads
2. **Format Detection**: Identify file type and appropriate parser
3. **Content Extraction**: 
   - PDF: PyMuPDF for text extraction
   - DOCX: python-docx for structured content
   - TXT: Direct text processing
4. **Text Cleaning**: Remove formatting artifacts, normalize text
5. **Content Analysis**: Parse into structured data (sections, skills, experience)

## Key Design Patterns

### API Design Pattern
- **Resource-based URLs**: `/api/resumes/`, `/api/jobs/`, `/api/evaluations/`
- **HTTP Methods**: GET, POST, PUT, DELETE for CRUD operations
- **Custom Actions**: @action decorator for non-CRUD endpoints (e.g., `/resumes/active/`)
- **Status Codes**: Proper HTTP status codes for different scenarios
- **Error Handling**: Consistent error response format
- **Pagination**: For large result sets
- **Authentication**: IsAuthenticated permission on all endpoints

### User Isolation Pattern
- **get_queryset()**: Override to filter by request.user automatically
- **perform_create()**: Override to assign user and enforce business rules
- **Row-Level Security**: Users can only access their own data
- **Shared Resources**: JobDescriptions shared across users, linked via UserJobInterest

### File Processing Pattern
- **Strategy Pattern**: Different parsers for different file formats
- **Pipeline Pattern**: Sequential processing steps
- **Error Recovery**: Graceful handling of parsing failures
- **Validation**: File type, size, and content validation
- **SHA-256 Hashing**: Content-based deduplication

### AI Evaluation Pattern
- **Prompt Hashing**: Cache evaluations by prompt hash
- **Modular Analysis**: Separate scoring (ATS, match) and suggestions
- **Token Tracking**: Monitor LLM API usage
- **Error Handling**: Retry logic for transient failures
- **Result Storage**: Store in Evaluation model for history

## Data Flow Patterns

### Resume Upload Flow
1. Frontend uploads file to `/api/resumes/upload/`
2. Backend validates file and stores metadata
3. File processing pipeline extracts content
4. Analysis engine processes content
5. Results stored in database
6. Frontend polls or receives webhook for completion

### Analysis Results Flow
1. Analysis engine generates scores and recommendations
2. Results serialized to JSON format
3. Frontend receives structured data
4. React components render scores and suggestions
5. User interactions trigger additional analysis or recommendations

## Error Handling Patterns
- **Graceful Degradation**: Continue processing even if some analysis fails
- **User-Friendly Messages**: Convert technical errors to actionable messages
- **Retry Logic**: Automatic retry for transient failures
- **Logging**: Comprehensive logging for debugging and monitoring

## Security Patterns
- **File Validation**: Strict file type and size validation
- **Input Sanitization**: Clean and validate all user inputs
- **CORS Configuration**: Proper cross-origin resource sharing setup
- **Rate Limiting**: Prevent abuse of analysis endpoints (future)

## Performance Patterns
- **Database Indexes**: Composite indexes on (user, is_active) for fast queries
- **Prompt Caching**: Cache AI evaluations by prompt_hash
- **Shared Resources**: JobDescriptions shared across users to reduce storage
- **Async Processing**: Non-blocking file processing (future: Celery)
- **Query Optimization**: get_queryset() filters at database level
- **Frontend Optimization**: Code splitting and lazy loading

## Enterprise Patterns Implemented

### Database Optimization
- **Composite Indexes**: `Index(fields=['user', 'is_active'])` for fast user-scoped queries
- **Field Indexes**: `db_index=True` on frequently queried fields (sha256, is_active)
- **Ordering**: Default ordering on models for consistent results

### Code Quality
- **Docstrings**: All methods documented (similar to JSDoc in TypeScript)
- **__str__ Methods**: Human-readable model representations for admin and logging
- **related_name**: Clean reverse ForeignKey lookups (e.g., `user.resumes.all()`)
- **Type Safety**: TypeScript on frontend, Django ORM on backend

### Security
- **Authentication Required**: IsAuthenticated on all ViewSets
- **User Isolation**: get_queryset() ensures users only see their own data
- **Content Hashing**: SHA-256 for integrity and deduplication
- **Input Validation**: Serializers validate all incoming data

### Business Logic Patterns
- **Single Active Resume**: Enforced in perform_create(), not database schema
- **Deactivate Previous**: `Resume.objects.filter(user=user).update(is_active=False)`
- **Automatic Assignment**: User assigned automatically from request.user
- **Growth-Ready Schema**: Supports future multi-resume without migration
