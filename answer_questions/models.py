from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Fach(models.Model):
    Name=models.CharField(null=True,blank=True,max_length=100)
    
    def __str__(self):
        return  f"{self.Name}, {self.pk}"

class Thema(models.Model):
    Name=models.CharField(null=True,blank=True,max_length=100)
    Fach = models.ForeignKey(Fach,null=True, blank=True, related_name='thema_fach',  on_delete=models.CASCADE)
    def __str__(self):
        return  self.Name
    
class Exercise_Type(models.Model):
    Name=models.CharField(null=True,blank=True,max_length=100)
    def __str__(self):
        return self.Name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    klasse = models.CharField(null=True, blank=True, max_length=100)
    Thema = models.ForeignKey(Thema,null=True, blank=True, related_name='exercises_thema',  on_delete=models.CASCADE)
    Fach = models.ForeignKey(Fach,null=True, blank=True, related_name='exercises_fach',  on_delete=models.CASCADE)

    
    Exercise_Type = models.ForeignKey(Exercise_Type,null=True, blank=True, related_name='exercises_type',  on_delete=models.CASCADE)
    head=models.CharField(null=True, blank=True, max_length=500)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    
    Author= models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE)
    last_time  = models.DateField(null=True, blank=True)
    next_time  = models.DateField(null=True, blank=True)
    last_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    correct_answer = models.CharField(max_length=100)
    question_number = models.IntegerField(null=True, blank=True)  # New field to hold the question number
    user_anwer=models.CharField(null=True,blank=True,max_length=400)

    def __str__(self):
        return f"{self.text}, {self.exercise}"
