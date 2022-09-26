from django.urls import path

from QuizApp.views import CategoryView, home, QuizView



urlpatterns = [
    path("", home, name="home"),
    path("category/", CategoryView.as_view() , name="category"),
    path("quiz/", QuizView.as_view() , name="quiz"),
]