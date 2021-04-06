from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def carry_data(request,data):
    return HttpResponse(f'<h1>The rcieved is {data} </>')
