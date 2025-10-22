# Project Brief: AI Resume Checker

## Project Overview
An AI-powered resume analysis and improvement platform that helps job seekers optimize their resumes for better job matching and ATS (Applicant Tracking System) compatibility.

## Core Requirements
- **Resume Upload & Processing**: Support multiple file formats (PDF, DOCX, TXT)
- **AI-Powered Analysis**: Analyze resume content for:
  - ATS compatibility and optimization
  - Skills gap identification
  - Industry-specific recommendations
  - Keyword optimization for job descriptions
  - Format and structure improvements
- **Interactive Dashboard**: User-friendly interface for viewing analysis results
- **Recommendation Engine**: Actionable suggestions for resume improvement
- **Job Matching**: Compare resume against job descriptions for compatibility scoring

## Technical Architecture
- **Frontend**: React + TypeScript + Vite (modern, fast development)
- **Backend**: Django REST Framework (robust API and admin interface)
- **Database**: SQLite (development) with PostgreSQL migration path
- **File Processing**: Support for PDF (PyMuPDF), DOCX (python-docx), and text parsing
- **Containerization**: Docker setup for consistent deployment

## Success Criteria
1. Successfully parse and extract text from common resume formats
2. Provide meaningful, actionable feedback on resume content
3. Generate ATS compatibility scores
4. Offer industry-specific optimization suggestions
5. Create an intuitive user experience for resume analysis workflow

## Project Scope
- MVP focuses on core resume analysis functionality
- Future iterations may include: user accounts, resume templates, job board integration, advanced AI features
- Current phase: Foundation and core analysis engine

## Constraints
- Must handle various resume formats reliably
- Analysis must be fast (< 30 seconds for typical resumes)
- Results must be actionable and specific
- Interface must be intuitive for non-technical users
