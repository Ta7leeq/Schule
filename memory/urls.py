from django.urls import path
from . import views

urlpatterns = [
    # URL path for displaying the list of fill the gaps exercises
    path('memory', views.memory, name='memory'),
  
]

