from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sample_api.models import *
from sample_api.Serializers import StudentSerializer
# Create your views here.
@api_view()
def view_dtl(request):
    return Response({'success':409, 'message':'api'})
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def view_student(request):
    if request.method=='GET':
        student_obj=Students.objects.all()
        serializer=StudentSerializer(student_obj, many=True)
        return Response({'msg':'Successfully retrived data', 'data':serializer.data},status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Person created Successfully', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        if pk:
            student_obj = get_object_or_404(Students, pk=pk)
            serializer = StudentSerializer(student_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Student updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'Student ID is required for PUT request'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'msg':'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)