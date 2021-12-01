from rest_framework import serializers
from rest_framework import viewsets
from todo_api.models import TodoListModel
from todo_api.serializers import TodoListSerializer


class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoListModel.objects.all()
    ordering_fields = ["-created"]
    filter_class = WorkTimeFilter
