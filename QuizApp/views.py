from unicodedata import category
from urllib import request
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from QuizApp.models import Category, Question, Quiz
from QuizApp.serializers import CategorySerializer, QuestionSerializer, QuizSerializer
# Create your views here.


def home(request):
    return HttpResponse("<h1>Home Page</h1>")


class CategoryListView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):

    def get_object(self, pk):
        category_instance = get_object_or_404(Category, pk=pk)
        return category_instance

    def get(self, request, pk):
        category = self.get_object(pk=pk)
        serialzer = CategorySerializer(category)
        return Response(serialzer.data)

    def put(self,request, pk):
        category = self.get_object(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuizListView(APIView):
    def get(self, request):
        quiz = Quiz.objects.all()
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizDetailView(APIView):
    def get_object(self, pk):
        quiz_instance = get_object_or_404(Quiz, pk=pk)
        return quiz_instance
    
    def get(self, request, pk):
        quiz = self.get_object(pk=pk)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)
    
    def put(self, request, pk):
        quiz = self.get_object(pk=pk)
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        quiz = self.get_object(pk=pk)
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestinListView(APIView):
    def get(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)