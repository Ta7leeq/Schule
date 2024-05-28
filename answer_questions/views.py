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
        
    
    if request.method == 'POST':
        try:
            user_answer = request.POST.get('answer')
            question = Question.objects.get(question_number=question_id,exercise_id=exercise_id)
            question.user_anwer=user_answer
            question.save()
        except Question.DoesNotExist:
            return redirect('index')  # Redirect to the exercise list if the question does not exist
        
        if request.POST.get('button')=="back":
            if question_id>1:
                return redirect('exercise_detail',exercise_id=exercise_id,question_id=question_id-1)
 
        elif request.POST.get('button')=="next":
            last_question_Number=Question.objects.filter(exercise_id=exercise_id).count()
            
            if question_id<last_question_Number:
                return redirect('exercise_detail', exercise_id=exercise_id, question_id=question.question_number+1)
                
            else:
                return redirect('exercise_complete',exercise_id=exercise_id)
            
                
    return render(request, 'answer_questions/exercise_detail.html', {'exercise': exercise, 
                                                                     'question': question,
                                                                     'question_id':question_id, 
                                                                     'exercise_id':exercise_id,
                                                                     
                                                                     })

def check_answer(request, exercise_id, question_id):
    
    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        
        
        print("value")
        try:
            question = Question.objects.get(question_number=question_id,exercise_id=exercise_id)
            question.user_anwer=user_answer
            question.save()
        except Question.DoesNotExist:
            return redirect('index')  # Redirect to the exercise list if the question does not exist

        
        last_question_Number=Question.objects.filter(exercise_id=exercise_id).count()
        
    
        if question.question_number<last_question_Number:
            #return redirect('exercise_detail', exercise_id=exercise_id, question_id=question.question_number+1)
            print("next")
        else:
            return redirect('exercise_complete',exercise_id=9)
                
                
        
            

def exercise_complete(request,exercise_id):
    
    if request.method=='POST':
        pass
        
    questions = Question.objects.filter(exercise=exercise_id)
    
    voll_mark=len(questions)
    
    score=0
    for question in questions:
        
        if question.user_anwer==question.correct_answer:
            score=score+1

    percent=(score/voll_mark)*100
    comment=comment_score(percent)
    print(percent,comment)

    return render (request, 'answer_questions/exercise_complete.html',
                {'questions':questions,
                    'score':score,
                    'voll_mark':voll_mark,
                    'percent':percent,
                    'comment':comment},
                    )


def comment_score(percent):
    if 0 <= percent < 50:
        return "You need to improve."
    elif 50 <= percent < 70:
        return "Good job, keep practicing!"
    elif 70 <= percent < 90:
        return "Great work!"
    elif 90 <= percent <= 100:
        return "Excellent!"
    else:
        return "Invalid score."