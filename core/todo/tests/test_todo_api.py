from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from accounts.models import User
from todo.models import Priority

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(email="admin@admin.com",password="a/@1234567",is_verified=True)
    return user


@pytest.mark.django_db
class TestTaskApi():

    client = APIClient()

    def test_get_todo_response_200_status(self):
        url = reverse('todo:api-v1:task-list')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_task_response_201_status(self,api_client,common_user):
        url = reverse('todo:api-v1:task-list')
        priority = Priority.objects.create(title="High", level=3)
        data = {
            "title": "test",
            "description": "description",
            "completed": True,
            "created_date": datetime.now(),
            "priority": priority.id

        }
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_task_response_403_status(self,api_client,common_user):
        url = reverse('todo:api-v1:task-list')
        priority = Priority.objects.create(title="High", level=3)
        data = {
            "title": "test",
            "description": "description",
            "completed": True,
            "created_date": datetime.now(),
            "priority": priority.id

        }

        response = api_client.post(url, data)
        assert response.status_code == 403
        
    def test_create_task_response_400_status(self,api_client,common_user):
        url = reverse('todo:api-v1:task-list')
        data = {
            "title": "test",
            "description": "description",
            "completed": True,

        }
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data)
        assert response.status_code == 400
