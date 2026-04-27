from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register('task',views.TaskViewset,basename='task')
router.register('priority',views.PriorityViewset,basename='priority')
urlpatterns = router.urls

# urlpatterns = [
#     path('', views.api_task_list_view, name='task-list'),
#     path('<int:id>/', views.postDetail, name='task-detail')
# ]