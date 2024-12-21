from django.shortcuts import render
from Product.models import *
from Product.serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .test import Message
# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ListProduct(request):
    query=Product.objects.all()
    serializer_class=ProductSerializer(query,many=True)
    return Response(serializer_class.data)
@api_view(['GET', 'POST'])
def ListMessage(request):
    message_obj=Message('adityarath428@gmail.com','Hi Hellow...')
    serializer_class=MessageSerializer(message_obj)
    return Response(serializer_class.data)   