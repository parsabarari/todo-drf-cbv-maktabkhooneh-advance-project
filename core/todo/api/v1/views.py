from rest_framework import viewsets
from rest_framework.response import Response
from ...models import TaskModel, Priority
from .serializers import TaskSerializer, PrioritySerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadOnly
from .paginations import DefaultPagination

class TaskViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['priority', 'author', 'completed']
    search_fields = ['title', 'description', 'priority__title']
    ordering_fields = ['published_date']
    pagination_class = DefaultPagination


class PriorityViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PrioritySerializer
    queryset = Priority.objects.all()

'''
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
        return Response({"detail":"item removed successfully"}, status=status.HTTP_204_NO_CONTENT)'''

     