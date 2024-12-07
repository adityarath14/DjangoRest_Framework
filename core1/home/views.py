from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import *
from home.serializers import *
from rest_framework import status
# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def view_person(request):
    if request.method=='GET':
        person_obj=Person.objects.all()
        serializer=PersonSerializer(person_obj, many=True)
        return Response({'msg':'Successfully retrieved data', 'data':serializer.data},status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Person created successfully','data':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        serializer=PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Person updated successfully','data': serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PATCH':
        person_obj = Person.objects.get(id=request.data['id'])
        serializer=PersonSerializer(person_obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Person updated successfully','data': serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        person_obj=Person.objects.get(id=request.data['id'])
        person_obj.delete()
        return Response({'msg': 'Person deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'msg': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)