from django.urls import path
from . import views

urlpatterns = [
    # URL path for displaying the list of fill the gaps exercises
    path('', views.penguin, name='penguin'),
    path('start', views.start, name='start'),

    path('checkPenguin', views.checkPenguin, name='checkPenguin'),


]

