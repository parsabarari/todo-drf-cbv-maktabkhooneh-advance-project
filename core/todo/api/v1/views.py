from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from ...models import TaskModel
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework import status


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def api_task_list_view(request):
    if request.method == 'GET':
        tasks = TaskModel.objects.all()
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def postDetail(request,id):
    task = get_object_or_404(TaskModel,pk=id)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        task.delete()
        return Response({"detail":"item removed successfully"}, status=status.HTTP_204_NO_CONTENT)