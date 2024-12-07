from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from app.models import *
from app.serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['GET','POST'])
def first(request):
    return Response({'Message':'Hai'})
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def studentData(request):
    LSO=Student.objects.all()
    MSSO=StudentMS(LSO,many=True)
    return Response(MSSO.data)