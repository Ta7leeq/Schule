
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from .models import gaps
from django.views import View

from django.http import JsonResponse

# Create your views here.

counter=0
class CompareView(View):
    def post(self, request):
        # Get the value from the POST data
        input_value = request.POST.get('input_value', '')

        # Compare the input value with another value
        target_value = 'some_value_to_compare'
        if input_value == target_value:
            response = "Input value matches the target value."
        else:
            response = "Input value does not match the target value."

        return HttpResponse(response)

def index(request):
    
    gap_first=gaps.objects.first()
    all_gaps=gaps.objects.all()
    unique_categories = list(gaps.objects.values_list('category', flat=True).distinct())
    filtered_records = gaps.objects.filter(category='to have')
    #gap_first=filtered_records.first()
    
    
    
    
    return render (request,"fill_the_gaps/index.html",
                    {   
                        "context":gap_first.sentence.split(),
                   "gap_word_number":gap_first.gapWord,
                   "all_sentences":all_gaps,
                   "categories":unique_categories
                        },
                        

                        )  
    


def questions(request,question_no):
    #check if answer is submitted!
    #all_gaps=gaps.objects.all()
    #question = all_gaps[question_no]

    
    
    response01=request.POST.get('submit')
    filtered_records = gaps.objects.filter(category=response01)
    
    #question=filtered_records[2]
    question=filtered_records[0]
    
    gap_number=question.gapWord
    print(question,question_no) 
    sentence=question.sentence.split()
    print(request.POST)
    if request.method=='POST':
        
        #fetch the user answer from the input element 
        
        response02=request.POST.get('gap_word')
        print("response2",response02)
        if sentence[gap_number-1]==response02:
            print("right")
            return redirect('questions', question_no=question_no+1)

      
    print(question_no+1)
    return render(request, "fill_the_gaps/questions.html", {
    "question":filtered_records[question_no],
    "question_no":question_no
    
})


def quiz01(request):

    return render (request,"fill_the_gaps/quiz01.html")

