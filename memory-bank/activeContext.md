# Active Context: AI Resume Checker

## Current Project State
**Status**: Initial setup phase - basic project structure exists but core functionality not yet implemented

### What Exists
- **Project Structure**: Basic Django + React setup with proper separation
- **Frontend**: React 19 + TypeScript + Vite boilerplate (default counter app)
- **Backend**: Django 4.2 with basic configuration and empty resume_api app
- **Dependencies**: All necessary packages installed for file processing
- **Docker**: Basic Dockerfile setup for both frontend and backend
- **Memory Bank**: Comprehensive documentation system established

### What's Missing (Critical Path)
1. **Resume Upload API**: Django REST API endpoint for file uploads
2. **File Processing Pipeline**: PDF/DOCX/TXT parsing and text extraction
3. **Analysis Engine**: Core logic for resume analysis and scoring
4. **Frontend UI**: Complete user interface for upload and results display
5. **Database Models**: Resume, Analysis, and Recommendation models
6. **API Integration**: Frontend-backend communication setup

## Immediate Next Steps

### Phase 1: Backend Foundation (Priority 1)
1. **Create Database Models**
   - Resume model (file metadata, upload info)
   - Analysis model (scores, extracted text)
   - Recommendation model (suggestions, categories)

2. **Implement File Upload API**
   - POST endpoint for resume uploads
   - File validation and storage
   - Return resume ID for frontend

3. **Build File Processing Pipeline**
   - PDF text extraction (PyMuPDF)
   - DOCX processing (python-docx)
   - Text cleaning and normalization

### Phase 2: Analysis Engine (Priority 2)
1. **ATS Compatibility Analysis**
   - Check for common ATS-friendly elements
   - Score formatting and structure
   - Identify problematic elements

2. **Keyword Analysis**
   - Extract skills and keywords
   - Industry-specific keyword matching
   - Missing keyword identification

3. **Recommendation Generation**
   - Rule-based suggestion system
   - Priority-based recommendations
   - Actionable improvement suggestions

### Phase 3: Frontend Development (Priority 3)
1. **Upload Interface**
   - Drag-and-drop file upload
   - Progress indicators
   - File validation feedback

2. **Results Dashboard**
   - Score visualization
   - Recommendation display
   - Interactive improvement suggestions

3. **API Integration**
   - Axios service functions
   - React Query for state management
   - Error handling and loading states

## Current Technical Decisions

### Architecture Decisions Made
- **Django REST Framework**: Chosen for robust API development
- **React Query**: Selected for server state management
- **SQLite**: Starting with SQLite for development simplicity
- **File Processing**: Multi-library approach for format support

### Pending Decisions
- **UI Framework**: CSS framework choice (Tailwind, Material-UI, or custom)
- **Authentication**: User accounts vs anonymous analysis
- **File Storage**: Local filesystem vs cloud storage
- **Analysis AI**: Rule-based vs ML-based analysis approach

## Development Patterns Established

### Code Organization
- **Frontend**: Component-based architecture with TypeScript
- **Backend**: Django app-based structure with clear separation
- **API Design**: RESTful endpoints with JSON responses
- **Error Handling**: Consistent error response format

### Quality Standards
- **TypeScript**: Strict typing for frontend code
- **ESLint**: Code linting and formatting rules
- **Django Best Practices**: Following Django conventions
- **Documentation**: Comprehensive memory bank system

## Known Issues & Considerations

### Technical Debt
- **Empty Models**: resume_api/models.py is empty
- **Basic Settings**: Django settings not optimized for resume processing
- **No CORS**: Cross-origin requests not configured
- **File Size Limits**: No upload size restrictions

### Future Enhancements
- **User Authentication**: Multi-user support
- **Resume Templates**: Pre-built resume formats
- **Job Matching**: Integration with job boards
- **Advanced AI**: Machine learning-based analysis

## Learning & Insights

### Project Insights
- **File Processing Complexity**: Multiple formats require different parsing strategies
- **Analysis Subjectivity**: Resume analysis involves subjective criteria
- **Performance Requirements**: Fast processing essential for user experience
- **Scalability Considerations**: File storage and processing need to scale

### Technical Learnings
- **PyMuPDF**: Powerful PDF processing but requires careful text extraction
- **python-docx**: Good for structured DOCX processing
- **Django REST**: Excellent for rapid API development
- **React Query**: Effective for server state management

## Current Focus
**Primary Goal**: Implement core resume upload and analysis functionality
**Secondary Goal**: Create intuitive user interface for resume analysis workflow
**Success Metric**: Successfully analyze a resume and provide meaningful recommendations
