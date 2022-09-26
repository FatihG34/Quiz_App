from dataclasses import fields
from rest_framework import serializers
from QuizApp.models import Category, Question, Quiz


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

class QuestionSerializer(serializers.ModelSerializer):
    quiz = serializers.StringRelatedField()
    quiz_id = serializers.IntegerField()
    class Meta:
        model = Question
        fields = ["id", "title", "difficulty", "created_date", "quiz", "quiz_id"]