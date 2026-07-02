from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import Student
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import StudentSerializers
# Create your views here.

def home (request):
    d= {'id':1,'name':'TD','marks':20}
    d= Student.objects.all()
    st=list(d.values())
    return JsonResponse(st,safe=False)


@api_view(['GET','POST'])
def home1(request):
    if request.method =='GET':
        student = Student.objects.all()
        serializer= StudentSerializers(student,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        student = Student.objects.all()
        serializer= StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    
    


@api_view(['GET','POST'])
def home2(request):
    if request.method =='GET':
        student = Student.objects.all()
        serializer= StudentSerializers(student,many=True)
    
    return Response(serializer.data)