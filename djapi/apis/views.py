from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Task
from .serializers import TaskSerializer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-list/<str:pk>/',
        'Create':'/task-create/',
        'update':'task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serialziers = TaskSerializer(tasks, many=True)
    return Response(serialziers.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serialize = TaskSerializer(data=request.data)

    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)
    
@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(pk=pk)
    serialize = TaskSerializer(instance=task, data=request.data)
    if serialize.is_valid():
        serialize.save()

    return Response(serialize.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response('Item deleted successfully')