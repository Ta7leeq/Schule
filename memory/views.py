from django.shortcuts import render


from django.shortcuts import render, redirect
#from .models import Exercise, Question, Fach, Thema,Exercise_Type
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from datetime import date, timedelta

def memory(request):
    
    
    return HttpResponse ("Hello Memory")