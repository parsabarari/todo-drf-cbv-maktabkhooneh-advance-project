from rest_framework import serializers
from ...models import TaskModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id','author','title','description','completed','priority','created_date']