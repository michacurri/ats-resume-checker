# Active Context: AI Resume Checker

## Current Project State
**Status**: Backend models and views implemented - MVP foundation complete, ready for AI integration
**Last Updated**: 2025-10-22

### What Exists
- **Project Structure**: Django + React setup with proper separation
- **Frontend**: React 19 + TypeScript + Vite (running on localhost:5174)
- **Backend**: Django 4.2 with DRF, enterprise-grade models and views
- **Git Repository**: Connected to GitHub (michacurri/ats-resume-checker)
- **Database Models**: Resume, JobDescription, UserJobInterest, Evaluation (complete)
- **ViewSets**: Authentication, user isolation, custom actions implemented
- **Dependencies**: All necessary packages installed for file processing
- **Docker**: Basic Dockerfile setup for both frontend and backend
- **Memory Bank**: Comprehensive documentation system established

### What's Missing (Critical Path)
1. **AI Integration**: LLM-based resume analysis and evaluation
2. **File Upload Handler**: Actual file upload endpoint with PDF/DOCX parsing
3. **Job Scraping Utility**: Web scraping for job descriptions
4. **Frontend UI**: Complete user interface for upload and results display
5. **API Integration**: Frontend-backend communication setup
6. **Authentication System**: User registration and login flow

## Immediate Next Steps

### Phase 1: AI Integration & File Processing (Priority 1)
1. **Implement AI Evaluation Flow**
   - Build prompt builder for resume + job analysis
   - Integrate LLM API (OpenAI/Anthropic)
   - Implement prompt hashing for caching
   - Parse and store AI responses in Evaluation model

2. **Build File Upload Handler**
   - Implement actual file upload endpoint
   - PDF text extraction (PyMuPDF)
   - DOCX processing (python-docx)
   - Text cleaning and normalization
   - SHA-256 hashing integration

3. **Job Scraping Utility**
   - Web scraping function for job descriptions
   - URL deduplication logic
   - Text extraction and cleaning
   - Integration with JobDescription model

### Phase 2: Frontend Development (Priority 2)
1. **Upload Interface**
   - Drag-and-drop file upload
   - Progress indicators
   - File validation feedback

2. **Results Dashboard**
   - Score visualization (ATS score, match score)
   - Missing keywords display
   - Suggestions and recommendations
   - Interview prep guidance

3. **API Integration**
   - Axios service functions
   - React Query for state management
   - Error handling and loading states

### Phase 3: Advanced Features (Priority 3)
1. **Career Trajectory Analysis**
   - Analyze job history patterns
   - Infer career goals from job interests
   - Personalized resume feedback

2. **TTL & Cleanup**
   - Implement 90-day TTL for stale jobs
   - Prune unused JobDescriptions
   - Archive old evaluations

3. **Dashboard Enhancements**
   - Skill gap visualization
   - Career growth path suggestions
   - Interview prep guidance generator

## Current Technical Decisions

### Architecture Decisions Made
- **Django REST Framework**: Chosen for robust API development
- **React Query**: Selected for server state management
- **SQLite**: Starting with SQLite for development simplicity
- **File Processing**: Multi-library approach for format support
- **Single Active Resume**: MVP enforces one active resume per user (business logic in view)
- **Shared Job Descriptions**: Jobs shared across users, deduplicated by hash/URL
- **User Job Interest Tracking**: Many-to-many relationship via UserJobInterest model
- **Enterprise Patterns**: Indexes, docstrings, related_name, proper authentication

### Pending Decisions
- **UI Framework**: CSS framework choice (Tailwind, Material-UI, or custom)
- **LLM Provider**: OpenAI vs Anthropic vs local models
- **File Storage**: Local filesystem vs cloud storage (S3)
- **Job Scraping**: BeautifulSoup vs Playwright vs API integrations
- **TTL Implementation**: Celery tasks vs Django management commands

## Development Patterns Established

### Code Organization
- **Frontend**: Component-based architecture with TypeScript
- **Backend**: Django app-based structure with clear separation
- **API Design**: RESTful endpoints with JSON responses, custom @action decorators
- **Error Handling**: Consistent error response format
- **User Isolation**: get_queryset() filters data by authenticated user

### Quality Standards
- **TypeScript**: Strict typing for frontend code
- **ESLint**: Code linting and formatting rules
- **Django Best Practices**: Following Django conventions
- **Documentation**: Comprehensive memory bank system
- **Enterprise Patterns**: 
  - Database indexes for performance (composite indexes on user+is_active)
  - Docstrings for all methods (similar to JSDoc)
  - related_name on ForeignKeys for clean reverse lookups
  - __str__ methods for admin readability
  - IsAuthenticated permission classes
  - SHA-256 hashing for content deduplication

## Known Issues & Considerations

### Technical Debt
- **No Migrations Run**: Models created but migrations not applied to database yet
- **Basic Settings**: Django settings not optimized for file uploads
- **No CORS**: Cross-origin requests not configured for frontend
- **File Size Limits**: No upload size restrictions configured
- **No File Upload Handler**: File upload endpoint not implemented yet
- **No AI Integration**: LLM API not integrated yet

### Future Enhancements
- **Multi-Resume Support**: Currently enforced single resume, can enable multiple later
- **Resume Templates**: Pre-built resume formats
- **Job Board Integration**: Direct integration with LinkedIn, Indeed, etc.
- **Advanced AI**: Fine-tuned models for industry-specific analysis
- **Enterprise Features**: Team accounts, bulk analysis, API access

## Learning & Insights

### Project Insights
- **File Processing Complexity**: Multiple formats require different parsing strategies
- **Business Model Evolution**: Started with simple resume analysis, evolved to career coaching platform
- **Performance Requirements**: Fast processing essential for user experience
- **Scalability Considerations**: Shared job descriptions reduce storage, user interests enable personalization
- **MVP vs Growth**: Single resume enforced in business logic, not schema - enables easy future expansion

### Technical Learnings
- **Django Patterns**: get_queryset() for user isolation, perform_create() for business logic
- **DRF Actions**: @action decorator creates custom endpoints beyond CRUD
- **Database Optimization**: Composite indexes (user, is_active) for fast queries
- **Python Docstrings**: Similar to JSDoc, accessible at runtime, used by IDEs and docs
- **related_name**: Makes reverse ForeignKey lookups intuitive (user.resumes vs user.resume_set)
- **Git Workflow**: Branch renaming (master→main), remote setup, gitignore optimization

## Current Focus
**Primary Goal**: Integrate AI evaluation engine for resume analysis
**Secondary Goal**: Implement file upload handler with PDF/DOCX parsing
**Tertiary Goal**: Build job scraping utility for job description extraction
**Success Metric**: End-to-end flow: upload resume → analyze against job → display results
