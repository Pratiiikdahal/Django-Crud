from django.shortcuts import render,redirect,get_object_or_404
from firstapp.models import *
from firstapp.forms import StudentForms
# Create your views here.

def index(request,id=None):
    if id:
        students_updated=get_object_or_404(students,id=id)
        form=StudentForms(request.POST or None,instance=students_updated)
    else:
        form=StudentForms(request.POST or None)
        
   
    # form=StudentForms()
    if request.method=='POST':
        if "delete" in request.POST:
            to_be_deleted=get_object_or_404(students,id=request.POST['delete'])
            to_be_deleted.delete()
            return redirect('index-view')
        
        form=form
        if form.is_valid():
            form.save()
            return redirect('index-view')
        
    student_values=students.objects.all()
    context={'student':student_values,
             'form':form}
    return render(request,'firstapp/index.html',context=context)
