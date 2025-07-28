from rest_framework import serializers
from .models import AccidentReport

class AccidentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentReport
        fields = '__all__'
        read_only_fields = ['severity_score']  # because it's auto-calculated
