from django.shortcuts import render,redirect
from firstapp.models import *
from firstapp.forms import StudentForms
# Create your views here.

def index(request,id=None):
    student_values=students.objects.all()
    form=StudentForms()
    if request.method=='POST':
        form=StudentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index-view')
    context={'student':student_values,
             'form':form}
    return render(request,'firstapp/index.html',context=context)
