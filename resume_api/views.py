from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Resume, JobDescription, Evaluation, UserJobInterest
from .serializers import ResumeSerializer, JobDescriptionSerializer, EvaluationSerializer, UserJobInterestSerializer
import hashlib
from .utils import scrape_job_text

class ResumeViewSet(viewsets.ModelViewSet):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]  # Require login
    
    def get_queryset(self):
        # Users can only see their own resumes
        return Resume.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Calculate SHA-256 hash
        text_content = serializer.validated_data.get('text_blob', '')
        sha256_hash = hashlib.sha256(text_content.encode()).hexdigest()
        
        # Deactivate all existing resumes for this user (MVP single-resume enforcement)
        Resume.objects.filter(user=self.request.user).update(is_active=False)
        
        # Save new resume as active
        serializer.save(
            user=self.request.user,
            sha256=sha256_hash,
            is_active=True
        )

    @action(detail=False, methods=['get'])
    def active(self, request):
        """GET /resumes/active/ - Get user's active resume"""
        resume = request.user.resumes.filter(is_active=True).first()
        if not resume:
            return Response({'error': 'No active resume'}, status=status.HTTP_404_NOT_FOUND)
        return Response(self.get_serializer(resume).data)


class JobDescriptionViewSet(viewsets.ModelViewSet):
    serializer_class = JobDescriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return jobs the user has expressed interest in
        return JobDescription.objects.filter(interested_users__user=self.request.user)

    def create(self, request, *args, **kwargs):
        source_url = request.data.get('source_url')
        text_blob = request.data.get('text_blob')

        if not text_blob and source_url:
            text_blob = scrape_job_text(source_url)  # Scrape and sanitize
            if not text_blob:
                return Response({'error': 'Unable to fetch job description'}, status=status.HTTP_400_BAD_REQUEST)

        if not text_blob:
            return Response({'error': 'No job description provided'}, status=status.HTTP_400_BAD_REQUEST)

        sha256 = hashlib.sha256(text_blob.encode()).hexdigest()

        job, created = JobDescription.objects.get_or_create(
            sha256=sha256,
            defaults={'source_url': source_url, 'text_blob': text_blob}
        )

        UserJobInterest.objects.get_or_create(user=request.user, job=job)

        serializer = self.get_serializer(job)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

class UserJobInterestViewSet(viewsets.ModelViewSet):
    serializer_class = UserJobInterestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return interests for the logged-in user
        return UserJobInterest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the user
        serializer.save(user=self.request.user)


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer