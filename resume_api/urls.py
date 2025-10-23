from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResumeViewSet, JobDescriptionViewSet, EvaluationViewSet

router = DefaultRouter()
router.register(r'resumes', ResumeViewSet)
router.register(r'jobs', JobDescriptionViewSet)
router.register(r'evaluations', EvaluationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]