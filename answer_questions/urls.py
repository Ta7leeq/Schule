from django.urls import path
from . import views

urlpatterns = [
    # URL path for displaying the list of fill the gaps exercises
    path('', views.index, name='index'),

    path('exercise_select', views.exercise_select, name='exercise_select'),
    
    path('exercise/<int:exercise_id>/question/<int:question_id>/', views.exercise_detail, name='exercise_detail'),


    
    path('exercise/<int:exercise_id>/question/<int:question_id>/check/', views.check_answer, name='check_answer'),

]