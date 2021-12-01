from rest_framework import serializers
from todo_api.models import TodoListModel

class TodoListSerializer(serializers.Serializer):
    class Meta:
        model = WorkTime
        fields = '__all__'
