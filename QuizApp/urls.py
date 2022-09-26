from django.urls import path

from QuizApp.views import home



urlpatterns = [
    path("", home, name="home")
]