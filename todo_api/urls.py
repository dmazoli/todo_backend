from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from todo_api.views.TodoListViewSet import TodoListViewSet
from todo_api.views.CategoryViewSet import CategoryViewSet

router = DefaultRouter()

router.register('todo-list', TodoListViewSet)
router.register('todo-category', CategoryViewSet)


urlpatterns = [
    url(r'todo-api', include(router.urls)),

]