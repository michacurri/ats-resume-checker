from rest_framework import serializers
from .models import Resume, JobDescription, Evaluation, UserJobInterest 

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = '__all__'


class UserJobInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserJobInterest
        fields = '__all__'
        read_only_fields = ['user']

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'