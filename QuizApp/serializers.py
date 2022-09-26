from rest_framework import serializers
from QuizApp.models import Category, Quiz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name"]


class QuizSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Quiz
        fields = ["id", "category", "category_id", "title", "created_date"]
