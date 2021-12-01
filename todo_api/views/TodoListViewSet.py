from rest_framework import viewsets
from todo_api.models.TodoListModel import TodoList
from todo_api.serializers.TodoListSerializer import TodoListSerializer


class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
    ordering_fields = ["-created"]
