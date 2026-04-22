from django.urls import path, include
from . import views

app_name = "api-v1"

urlpatterns = [
    path('', views.api_task_list_view, name='task-list'),
    path('<int:id>/', views.postDetail, name='task-detail')
]