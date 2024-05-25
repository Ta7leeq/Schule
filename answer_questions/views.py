from django.shortcuts import render


from django.shortcuts import render, redirect
from .models import Exercise, Question, Fach, Thema,Exercise_Type
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

def index(request):
    exercises = Exercise.objects.all()
    
    return render(request, 'answer_questions/index.html', {'exercises': exercises})


def exercise_select(request,grade,Fach_Name,Thema_Name,Exercise_Type_Name):
    if request.method == 'POST':
        user_fach_Name=request.POST.get('select_fach')
        user_Thema_Name=request.POST.get('select_thema')
        user_Exercise_Type_Name=request.POST.get('select_exercise_type')
    


        return redirect('exercise_select',grade="Alle" ,Fach_Name=user_fach_Name,Thema_Name=user_Thema_Name,Exercise_Type_Name=user_Exercise_Type_Name)
        
    exercises = Exercise.objects.all()
    
    Facher=list(Fach.objects.all())
    Fach_Names = [fach.Name for fach in Facher]
    
    Themas=list(Thema.objects.all())
    Thema_Names = [thema.Name for thema in Themas]

    Exercise_Types=list(Exercise_Type.objects.all())
    Exercise_Types_Names = [exercise_type.Name for exercise_type in Exercise_Types]

    print(Fach_Name,Thema_Name,Exercise_Type_Name)
    
    if Fach_Name=="Alle" and Thema_Name=="Alle" and Exercise_Type_Name=="Alle":
        print("No Enter")
        filterd_exercises=exercises
    else:
        #user_fach_id=Fach.objects.filter(Name=Fach_Name).first().pk
        #user_thema_id=Thema.objects.filter(Name=Thema_Name).first().pk
        #user_exercise_type_id=Exercise_Type.objects.filter(Name=Exercise_Type_Name).first().pk

        
        #filterd_exercises=exercises
        print(Fach_Name,Thema_Name,Exercise_Type_Name)
        user_fach_id = Fach.objects.filter(Name=Fach_Name).first().pk if Fach_Name!="Alle" else 6
        user_thema_id = Thema.objects.filter(Name=Thema_Name).first().pk if Thema_Name!="Alle" else 4
        user_exercise_type_id = Exercise_Type.objects.filter(Name=Exercise_Type_Name).first().pk if Exercise_Type_Name!="Alle" else 3
        
        filterd_exercises=Exercise.objects.filter(Fach=user_fach_id,Thema=user_thema_id,Exercise_Type=user_exercise_type_id)

        
    return render(request,'answer_questions/exercise_select.html', {'exercises': filterd_exercises,
                                                                    'Facher':Fach_Names,
                                                                    'Themas':Thema_Names,
                                                                    'Exercise_Types':Exercise_Types_Names,

                                                                     })



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
            

