from django.db import models

# Create your models here.
from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    correct_answer = models.CharField(max_length=100)
    question_number = models.IntegerField(null=True, blank=True)  # New field to hold the question number

    def __str__(self):
        return self.text
