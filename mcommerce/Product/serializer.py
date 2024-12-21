from rest_framework import serializers
from Product.models import *
#Model Based Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
#Simple Serializer
class MessageSerializer(serializers.Serializer):
    email=serializers.EmailField()
    content=serializers.CharField(max_length=200)
    created=serializers.DateTimeField()