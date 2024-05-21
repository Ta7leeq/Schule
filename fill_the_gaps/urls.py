from django.urls import path
from . import views

urlpatterns=[
    path("", views.index,name="index"), 
    path("<str:category_name>", views.categories,name="categories"),
    path('"<str:category_name>"/question/<int:question_id>/check/', views.check_answer, name='check_answer'),


    path("quiz01", views.quiz01,name="quiz01"), 
]