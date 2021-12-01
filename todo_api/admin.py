from django.contrib import admin

from todo_api.models.TodoListModel import TodoList
from todo_api.models.CategoryModel import Category

admin.site.register(TodoList)
admin.site.register(Category)