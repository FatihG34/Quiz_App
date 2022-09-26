from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from QuizApp.models import Category, Quiz


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class QuizSerializer(ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Quiz
        fields = ["id", "category", "category_id", "title", "created_date"]
