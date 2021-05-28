from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer

from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

@api_view(['GET'])
def getTaskByID(request, id):
    getTask = Task.objects.filter(id= id)
    serializer = TaskSerializer(getTask, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    newTask = TaskSerializer(data=request.data)
    if newTask.is_valid():
        newTask.save()
    return Response(newTask.data)

@api_view(['PUT'])
def updateTask(request, id):
    taskObj = Task.objects.get(id= id)
    updatedTaskObj = TaskSerializer(instance=taskObj, partial=True, data=request.data)
    if updatedTaskObj.is_valid(raise_exception=True):
        updatedTaskObj.save()
        updated_data = updatedTaskObj.data
        return Response(updated_data)
    return Response(updatedTaskObj.data)

@api_view(['DELETE'])
def deleteTask(request, id):
    taskObj = Task.objects.get(id= id)
    taskObj.delete()
    return Response("Task Deleted Successfully")