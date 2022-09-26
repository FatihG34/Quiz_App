from tabnanny import verbose
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Quiz(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quizzes"


class Question(models.Model):
    DIFFICULTY = [
        ("easier", "Easier"),
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("expert", "Expert"),
        ("harder", "Harder"),
    ]
    title = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY)
    created_date = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(
        Quiz, related_name="related_quiz", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Answer(models.Model):
    answer_text = models.TextField()
    is_right = models.BooleanField()
    updated_date = models.DateTimeField(auto_now_add=False)
    related_question = models.ForeignKey(
        Question, related_name="related_question", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.related_question}'s answer"
