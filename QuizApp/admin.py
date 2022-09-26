from django.contrib import admin

from QuizApp.models import Answer, Category, Question, Quiz

# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)