from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def facto(request,num1):
    fact=1
    for i in range(int(num1),1,-1):
        fact*=i
    return HttpResponse(f"<h1>the factorial of {num1} is {fact}</h1>")
def add(request,num1,num2):
    try:
        num1=int(num1)
    except:
        num1=float(num1)
    try:
        num2=int(num2)
    except:
        num2=float(num2)
    return HttpResponse(num1+num2)
