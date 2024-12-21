from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from EmployeeDetails.models import *
from EmployeeDetails.serializers import *
# Create your views here.
@api_view()
def view_dtl(request):
    return Response({'success':409,'message':'api'})
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def view_Emp(request):
    if request.method=='GET':
        Emp_obj=Emp.objects.all()
        serializer=EmpSerializer(Emp_obj,many=True)
        return Response({'msg':'Successfully Retrived Data','data':serializer.data},status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Employee created Successfully','data':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        Emp_obj=Emp.objects.get(pk=request.data.get('id'))
        serializer=EmpSerializer(Emp_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Employee Updated Successfully','data':serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PATCH':
        Emp_obj=Emp.objects.get(pk=request.data.get('id'))
        serializer=EmpSerializer(Emp_obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Employee Updated Successfully','data':serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        Emp_obj=Emp.objects.get(pk=request.data.get('id'))
        Emp_obj.delete()
        return Response({'msg':'Person Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)
    return Response({'msg':'Invalid Request Method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)