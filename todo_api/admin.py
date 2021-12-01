from django.contrib import admin

from todo_api.models import TodoListModel, CategoryModel

admin.site.register(TodoListModel)
admin.site.register(CategoryModel)