from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    created_date= models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name="category" , on_delete=models.CASCADE)

class Question(models.Model):
    DIFFICULTY = [
        ("easier", "Easier"),
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("expert", "Expert"),
        ("harder", "Harder"),
    ]
    title = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50,choices=DIFFICULTY)
    created_date = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(Quiz,related_name="related_quiz" , on_delete=models.CASCADE)

class Answer(models.Model):
    answer_text = models.TextField()
    is_right = models.BooleanField()
    updated_date = models.DateTimeField(auto_now_add=False)
    related_question = models.ForeignKey(Question, related_name="related_question", on_delete=models.CASCADE)