from rest_framework import serializers
from todo_api.models.CategoryModel import Category

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'
