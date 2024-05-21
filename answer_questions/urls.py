from django.urls import path
from . import views

urlpatterns = [
    # URL path for displaying the list of fill the gaps exercises
    path('', views.index, name='index'),

    # URL path for choosing an exercise and displaying exercise details
    #path('exercise/<int:exercise_id>/', views.exercise_detail, name='exercise_detail'),

    path('exercise/<int:exercise_id>/question/<int:question_id>/', views.exercise_detail, name='exercise_detail'),


    # URL path for checking the answer to a question
    path('exercise/<int:exercise_id>/question/<int:question_id>/check/', views.check_answer, name='check_answer'),

    # Optional: URL path for indicating exercise completion
    #path('exercise/completed/', views.exercise_completed, name='exercise_completed'),
]