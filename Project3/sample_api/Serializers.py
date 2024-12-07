from rest_framework import serializers
from sample_api.models import *
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields='__all__'