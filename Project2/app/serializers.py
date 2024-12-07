from rest_framework import serializers
from app.models import *
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'