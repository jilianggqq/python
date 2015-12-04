from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Task
from models import Info
from api.serializers import TaskSerializer
from api.serializers import InfoSerializer
import logging
logging.basicConfig(level=logging.DEBUG)


@api_view(['GET', 'POST'])
def hello_world(request):
    infos = Info.objects.all()
    serializer = InfoSerializer(infos, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def task_list(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        logging.debug(type(tasks))
        logging.debug(tasks)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    """
    Get, udpate, or delete a specific task
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
