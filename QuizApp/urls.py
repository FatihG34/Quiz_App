from django.urls import path

from QuizApp.views import CategoryListView, home, QuizListView, CategoryDetailView, QuizDetailView



urlpatterns = [
    path("", home, name="home"),
    path("category/", CategoryListView.as_view(), name="category"),
    path("category/<int:pk>", CategoryDetailView.as_view(), name="category-detail"),
    path("quiz/", QuizListView.as_view(), name="quiz"),
    path("quiz/<int:pk>", QuizDetailView.as_view(), name="quiz-detail"),
]