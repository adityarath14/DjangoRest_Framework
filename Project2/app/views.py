from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from app.models import *
from app.serializers import *
# Create your views here.
@api_view()
def view_dtl(request):
    return Response({'success':409,'message':'api'})
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def view_person(request):
    if request.method=='GET':
        person_obj=Person.objects.all()
        serializer=PersonSerializer(person_obj,many=True)
        return Response({'msg':'Successfully Retrived Data', 'data':serializer.data},status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Person Created Successfully', 'data':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        person_id = request.data.get('id')
        person_obj = Person.objects.get(pk=person_id)
        serializer =PersonSerializer(person_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Person Updated Successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PATCH':
        person_id=request.data.get('id')
        person_obj = Person.objects.get(pk=person_id)
        serializer=PersonSerializer(person_obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Person Updated Successfully', 'data':serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        person_id=request.data.get('id')
        person_obj=Person.objects.get(pk=person_id)
        person_obj.delete()
        return Response({'msg':'Person Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)
    return Response({'msg':'Invalid request method'},status=status.HTTP_405_METHOD_NOT_ALLOWED)