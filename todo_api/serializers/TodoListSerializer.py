from rest_framework import serializers
from todo_api.models.TodoListModel import TodoList

class TodoListSerializer(serializers.Serializer):
    class Meta:
        model = TodoList
        fields = '__all__'
