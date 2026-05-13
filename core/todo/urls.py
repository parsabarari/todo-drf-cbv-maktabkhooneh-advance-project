from django.urls import path, include
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task/api/', views.TaskListApiView.as_view(), name='task_list_api'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/toggle/', views.TaskCompleteToggleView.as_view(), name='task_complete'),
    path('api/v1/',include('todo.api.v1.urls'),name='api-v1')
]