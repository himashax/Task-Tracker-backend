from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
