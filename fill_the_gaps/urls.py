from django.urls import path
from . import views

urlpatterns=[
    path("", views.index,name="index"), 
    path("<int:question_no>", views.questions,name="questions"),

    path("quiz01", views.quiz01,name="quiz01"), 
]