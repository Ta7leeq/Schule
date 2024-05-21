
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from .models import gaps
from django.views import View

from django.http import JsonResponse

# Create your views here.


def index(request):
    
    
    
    unique_categories = list(gaps.objects.values_list('category', flat=True).distinct())
    
    
    return render (request,"fill_the_gaps/index.html",
                    {   
                   "categories":unique_categories
                        },
                       
                        )  
    

def categories(request,category_name):
    print("Anfang")
    
    response01=request.POST.get('submit')
    filtered_records = gaps.objects.filter(category=response01)
    first_question=filtered_records[0]
    return render(request, "fill_the_gaps/questions.html", {
        
        "category_name":category_name,
        "question":first_question
        
    })

def check_answer(request,category_name,question_id):
    if request.method == 'POST':
        user_answer = request.POST.get('input')
        question = gaps.objects.get(id=question_id)
        
        if user_answer == question.correct_answer:
            next_question = question.get_next_question()  # Implement a method to get the next question
            if next_question:
                return redirect('exercise_detail', exercise_id=exercise_id, question_id=next_question.id)
            else:
                return redirect('exercise_completed')  # Redirect to a page indicating exercise completion
        else:
            # Handle incorrect answer
            return render(request, 'exercise_detail.html', {'exercise': exercise, 'question': question})
    else:
        return redirect('index')  # Redirect to the exercise list if the request method is not POST



def quiz01(request):

    return render (request,"fill_the_gaps/quiz01.html")

