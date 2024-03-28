from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Items
from .serializers import ItemsSerializer

# Create your views here.
class ItemsAV(APIView):

    def get(self,request):
        item = Items.objects.all()
        serializer = ItemsSerializer(item, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ItemsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors)

    def put(self,request):
        item = Items.objects.get(pk=request.data['id'])
        serializer = ItemsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response (serializer.erros, status = status.HTTP_404_NOT_FOUND)

    def delete(self,request):
        item = Items.objects.get(pk=request.data['id'])
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemscategoryAV(APIView):
    def get(self,request,category):
        item = Items.objects.filter(category=category)
        serializer = ItemsSerializer(item, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ItemsSortAV(APIView):
    def get(self,request):
        item = Items.objects.all().order_by('-price')
        serializer = ItemsSerializer(item, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)





