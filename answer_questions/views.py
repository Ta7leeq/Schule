from django.shortcuts import render


from django.shortcuts import render, redirect
from .models import Exercise, Question
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

def index(request):
    exercises = Exercise.objects.all()
    
    return render(request, 'answer_questions/index.html', {'exercises': exercises})

def exercise_detail(request, exercise_id, question_id):
    exercise = Exercise.objects.get(id=exercise_id)
    question = Question.objects.get(question_number=question_id,exercise_id=exercise_id)
    
    return render(request, 'answer_questions/exercise_detail.html', {'exercise': exercise, 
                                                                     'question': question,
                                                                     'question_id':question_id, 
                                                                     'exercise_id':exercise_id
                                                                     })

def check_answer(request, exercise_id, question_id):
    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        try:
            question = Question.objects.get(question_number=question_id,exercise_id=exercise_id)
        except Question.DoesNotExist:
            return redirect('index')  # Redirect to the exercise list if the question does not exist

        if user_answer == question.correct_answer:
            last_question_Number=Question.objects.filter(exercise_id=exercise_id).count()
            print(question.question_number,last_question_Number)

            if question.question_number<last_question_Number:
                return redirect('exercise_detail', exercise_id=exercise_id, question_id=question.question_number+1)
            else:
                
                return HttpResponse("Exercise complete")
                
        else:
            # Handle incorrect answer
            
            return redirect('exercise_detail', exercise_id=exercise_id, question_id=question.question_number)
            

        
