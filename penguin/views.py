

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from datetime import date, timedelta
import random

def penguin(request):
    
    #equation=generate_random_pair()
        
    
    return render(request,'p.html',{"style":"answer_questions/p.css"})

def start(request):
    equation=generate_random_pair()
    print(equation)
    
    return render(request,'p.html',{"equation":equation
                                    ,"style":"answer_questions/p.css"},)


def checkPenguin(request):
    if request.method=='POST':
        keys = ["L1", "R1", "L2", "R2","L3","R3","M"]
        values = {key: int(request.POST.get(key)) for key in keys}
        L1 = values["L1"]
        R1 = values["R1"]
        L2 = values["L2"]
        R2 = values["R2"]
        L3 = values["L3"]
        R3 = values["R3"]
        
        M = values["M"]
        if (check_conditions(M, L1, R1, L2, R2, L3, R3)):
            return render(request,'p.html',{"equation":""
                                    ,"style":"answer_questions/p_right.css",
                                    "check":True})
        
        else:
            return render(request,'p.html',{"equation":""
                                    ,"style":"answer_questions/p_wrong.css",
                                    "check":False})




def generate_random_pair():
    factor=random.randint(2,9)

    sum = random.randint(11, 99)
    sum_multiplied=sum*factor

    num1=random.randint(1, sum - 1)
    num1_multiplied=num1*factor

    num2 = sum-num1
    num2_multiplied=num2*factor

    return {
        "factor":factor,
        "num1": num1,
        "num2": num2,
        "sum": sum,
        "num1_multiplied": num1_multiplied,
        "num2_multiplied": num2_multiplied,
        "sum_multiplied": sum_multiplied
    }

def check_conditions(M, L1, R1, L2, R2, L3, R3):
    # Check the conditions
    
    if R1 == L1 * M and R2 == L2 * M and R3 == L3 * M and R3 == R1 + R2 and L3 == L1 + L2:
        return True
    else:
        return False
