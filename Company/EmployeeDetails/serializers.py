from rest_framework import serializers
from EmployeeDetails.models import Emp
class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'