from rest_framework import viewsets
from todo_api.models.CategoryModel import Category
from todo_api.models.TodoListModel import TodoList
from todo_api.serializers.CategorySerializer import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    ordering_fields = ["-created"]
