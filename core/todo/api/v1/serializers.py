from rest_framework import serializers
from ...models import TaskModel, Priority
from accounts.models import Profile

class TaskSerializer(serializers.ModelSerializer):
    
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    
    class Meta:
        model = TaskModel
        fields = ['id','author','title','description','snippet','completed','relative_url','absolute_url','priority','created_date']

        read_only_fields = ['author']

    def get_abs_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        rep['state'] = 'list'
        if request.parser_context.get('kwargs').get('pk'):
            rep['state'] = 'single'
        
        rep['priority'] = PrioritySerializer(instance.priority,context={'request':request}).data
        return rep

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ['id','title','level']