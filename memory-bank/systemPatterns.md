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
- **API Design**: RESTful endpoints with JSON responses
- **File Processing**: Multi-format support (PDF, DOCX, TXT)
- **Database**: SQLite for development, PostgreSQL for production
- **Authentication**: Django's built-in auth system (future enhancement)

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
- **Resource-based URLs**: `/api/resumes/`, `/api/analysis/`
- **HTTP Methods**: GET, POST, PUT, DELETE for CRUD operations
- **Status Codes**: Proper HTTP status codes for different scenarios
- **Error Handling**: Consistent error response format
- **Pagination**: For large result sets

### File Processing Pattern
- **Strategy Pattern**: Different parsers for different file formats
- **Pipeline Pattern**: Sequential processing steps
- **Error Recovery**: Graceful handling of parsing failures
- **Validation**: File type, size, and content validation

### Analysis Engine Pattern
- **Modular Analysis**: Separate analyzers for different aspects
- **Scoring System**: Normalized scores (0-100) across different metrics
- **Recommendation Engine**: Rule-based suggestions with confidence scores
- **Caching**: Store analysis results for performance

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
- **Async Processing**: Non-blocking file processing
- **Caching**: Cache analysis results and parsed content
- **Database Optimization**: Proper indexing and query optimization
- **Frontend Optimization**: Code splitting and lazy loading
