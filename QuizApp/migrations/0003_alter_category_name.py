# Generated by Django 4.1.1 on 2022-09-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("QuizApp", "0002_alter_category_options_alter_quiz_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]