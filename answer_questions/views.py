from django.shortcuts import render


from django.shortcuts import render, redirect
from .models import Exercise, Question, Fach, Thema,Exercise_Type
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from datetime import date, timedelta

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
        
        filterd_exercises=Exercise.objects.filter(Author=request.user)
        
    else:
        #user_fach_id=Fach.objects.filter(Name=Fach_Name).first().pk
        #user_thema_id=Thema.objects.filter(Name=Thema_Name).first().pk
        #user_exercise_type_id=Exercise_Type.objects.filter(Name=Exercise_Type_Name).first().pk

        
        #filterd_exercises=exercises
        print(Fach_Name,Thema_Name,Exercise_Type_Name)
        user_fach_id = Fach.objects.filter(Name=Fach_Name).first().pk if Fach_Name!="Alle" else 6
        user_thema_id = Thema.objects.filter(Name=Thema_Name).first().pk if Thema_Name!="Alle" else 4
        user_exercise_type_id = Exercise_Type.objects.filter(Name=Exercise_Type_Name).first().pk if Exercise_Type_Name!="Alle" else 3
        
        filterd_exercises=Exercise.objects.filter(Fach=user_fach_id,Thema=user_thema_id,Exercise_Type=user_exercise_type_id,name="Mathe_Pferd")

        
    return render(request,'answer_questions/exercise_select.html', {'exercises': filterd_exercises,
                                                                    'Facher':Fach_Names,
                                                                    'Themas':Thema_Names,
                                                                    'Exercise_Types':Exercise_Types_Names,

                                                                     })


def memorize(request):
    if request.method == 'POST':
        user_fach_Name=request.POST.get('select_fach')
        user_Thema_Name=request.POST.get('select_thema')
        user_Exercise_Type_Name=request.POST.get('select_exercise_type')
    


        return redirect('exercise_select',grade="Alle" ,Fach_Name=user_fach_Name,Thema_Name=user_Thema_Name,Exercise_Type_Name=user_Exercise_Type_Name)
        
    exercises = Exercise.objects.all()
    
    
    
    if 1:
        
        filterd_exercises=Exercise.objects.filter(Author=request.user,next_time__lte=date.today())
        
    else:
        #user_fach_id=Fach.objects.filter(Name=Fach_Name).first().pk
        #user_thema_id=Thema.objects.filter(Name=Thema_Name).first().pk
        #user_exercise_type_id=Exercise_Type.objects.filter(Name=Exercise_Type_Name).first().pk

        
        #filterd_exercises=exercises
        
        user_fach_id = Fach.objects.filter(Name=Fach_Name).first().pk if Fach_Name!="Alle" else 6
        user_thema_id = Thema.objects.filter(Name=Thema_Name).first().pk if Thema_Name!="Alle" else 4
        user_exercise_type_id = Exercise_Type.objects.filter(Name=Exercise_Type_Name).first().pk if Exercise_Type_Name!="Alle" else 3
        
        filterd_exercises=Exercise.objects.filter(Fach=user_fach_id,Thema=user_thema_id,Exercise_Type=user_exercise_type_id,name="Mathe_Pferd")

        
    return render(request,'answer_questions/exercise_select.html', {'exercises': filterd_exercises,
                                                                    

                                                                     })




def exercise_detail(request, exercise_id, question_id):
     
    exercise = Exercise.objects.get(id=exercise_id)
    excercise_type=exercise.Exercise_Type
    #print(type(excercise_type))
    if str(excercise_type)=="Question_Answer":
        
        print(exercise.Exercise_Type)
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
                    print(exercise)
                    return redirect('exercise_complete',exercise_id=exercise_id)
                
                    
        return render(request, 'answer_questions/exercise_detail.html', {'exercise': exercise, 
                                                                        'question': question,
                                                                        'question_id':question_id, 
                                                                        'exercise_id':exercise_id,
                                                                        
                                                                       })
    elif str(excercise_type)=="fill_the_gaps":
        
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
                     
                    return redirect('fill_the_gaps_complete',exercise_id=exercise_id)
                
                    
        return render(request, 'answer_questions/fill_the_gaps.html', {'exercise': exercise, 
                                                                        'question': question,
                                                                        'question_id':question_id, 
                                                                        'exercise_id':exercise_id,
                                                                        
                                                                       })

       

def exercise_complete(request,exercise_id):
    
    if request.method=='POST':
        pass

    current_exercise=Exercise.objects.get(id=exercise_id)   
    questions = Question.objects.filter(exercise=exercise_id)
    
    voll_mark=len(questions)
    
    score=0
    for question in questions:
        
        if question.user_anwer==question.correct_answer:
            score=score+1

    percent=(score/voll_mark)*100
    comment=comment_score(percent)
    
    
    current_exercise.last_score=percent
    current_exercise.next_time=calculate_next_time(percent, current_exercise.next_time)
    
    current_exercise.save()

    

    return render (request, 'answer_questions/exercise_complete.html',
                {'questions':questions,
                    'score':score,
                    'voll_mark':voll_mark,
                    'percent':percent,
                    'comment':comment},
                    )


def fill_the_gaps_complete(request,exercise_id):
    
    if request.method=='POST':
        pass

    current_exercise=Exercise.objects.get(id=exercise_id)   
    questions = Question.objects.filter(exercise=exercise_id)
    
    voll_mark=len(questions)
    
    score=0
    for question in questions:
        words=question.text.split()
        #print(type(question.user_anwer),type(words[int(question.correct_answer)]))
        if question.user_anwer==words[int(question.correct_answer)-1]:
            score=score+1

    percent=(score/voll_mark)*100
    comment=comment_score(percent)
    
    
    current_exercise.last_score=percent
    current_exercise.next_time=calculate_next_time(percent, current_exercise.next_time)
    
    current_exercise.save()

    

    return render (request, 'answer_questions/fill_the_gaps_complete.html',
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
    

def calculate_next_time(score_percent, last_time_date):
    # Convert score_percent (1-100) to quality (1-5)
    quality = (score_percent / 100) * 4 + 1  # Ensures quality is between 1 and 5
    
    # Calculate Ease Factor (EF) using the given formula
    EF = 2.5 + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    
    # Set a minimum EF value to avoid invalid or too small intervals
    if EF < 1.3:
        EF = 1.3
    
    # Calculate the next review time (nextTime)
    # Starting with a base of 24 hours, multiplied by EF for scaling
    next_time = last_time_date + timedelta(hours=24 * EF)
    
    return next_time

#I dont know what this for is! 
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