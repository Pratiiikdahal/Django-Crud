from django.shortcuts import render
from firstapp.models import *
# Create your views here.

def index(request):
    student_values=students.objects.all()
    context={'student':student_values}
    return render(request,'firstapp/index.html',context=context)
