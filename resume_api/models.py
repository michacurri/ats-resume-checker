from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    filename = models.CharField(max_length=255)
    text_blob = models.TextField()
    sha256 = models.CharField(max_length=64, db_index=True)  # Indexed, not unique
    is_active = models.BooleanField(default=True, db_index=True)  # Future multi-resume feature
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
        indexes = [
            models.Index(fields=['user', 'is_active']),  # Fast lookup of user's active resume
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.filename}"

class JobDescription(models.Model):
    source_url = models.URLField(blank=True, null=True, unique=True)  # Optional for pasted descriptions, but always unique (one-to-many)
    text_blob = models.TextField()  # Raw job description text
    sha256 = models.CharField(max_length=64, db_index=True)  # Deduplication and caching
    fetched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fetched_at']
        indexes = [
            models.Index(fields=['sha256']),  # Fast lookup for deduplication
        ]

    def __str__(self):
        return self.source_url or f"Manual Entry ({self.sha256[:8]})"

class UserJobInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_interests')
    job = models.ForeignKey(JobDescription, on_delete=models.CASCADE, related_name='interested_users') # related_name reverse lookupgood for analytics and reporting
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.user.username} → {self.job.source_url or self.job.sha256[:8]}"

class Evaluation(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    prompt_hash = models.CharField(max_length=64)
    model_used = models.CharField(max_length=50)
    ats_score = models.IntegerField()
    match_score = models.IntegerField()
    missing_keywords = models.JSONField()
    suggestions = models.TextField()
    tokens_used = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)