from django.shortcuts import render
from API.models import Player
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from API.serializers import Playerserializer
# Create your views here.
@api_view(['GET',"POST"])
def api_demo(request):
    if request.method=="GET":
        person=Player.objects.all()
        data2=Playerserializer(person,many=True)
        # if data2.is_valid():
        #     data2.save()
        return Response(data2.data)
    elif request.method=="POST":
         person=Player.objects.all()
         data2=Playerserializer(data=request.data)
         if data2.is_valid():
            data2.save()
            return Response(data2.data,status=status.HTTP_201_CREATED)
         return Response(data2.error,status=status.HTTP_400_CREATED)


@api_view(['GET'])
def api_detail(request,id):
    try:
        player=Player.objects.get(id=id)
        
    except:
        return Response({"message":'record not found'},status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer= Playerserializer(player)
        return Response(serializer.data)

    