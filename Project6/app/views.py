from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
# Create your views here.
@permission_classes([IsAuthenticated])
class Crud(ViewSet):
    def list(self,request):
            OBJ=Product.objects.all()
            Serialized_obj=Product_Serializers(OBJ,many=True)
            return Response(Serialized_obj.data)
    def create(self,request):
        data=Product_Serializers(data=request.data)
        if data.is_valid():
            data.save()
            return Response({'Done':'Successsfull'})
    def update(self,request,pk=None):
        OBJ=Product.objects.get(id=pk)
        Update_Obj=Product_Serializers(OBJ,data=request.data)
        if Update_Obj.is_valid():
            Update_Obj.save()
            return Response({'Done':'Update Successsfull'})
    def partial_update(self,request,pk=None):
        OBJ=Product.objects.get(id=pk)
        Update_Obj=Product_Serializers(OBJ,data=request.data,partial=True)
        if Update_Obj.is_valid():
            Update_Obj.save()
            return Response({'Done':'Update Successsfull'})
    def delete(self,request,pk=None):
        Obj=Product.objects.get(id=pk).delete()
        return Response({'Done':'Delete Successsfull'})