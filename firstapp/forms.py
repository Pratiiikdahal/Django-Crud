from django import forms
from firstapp.models import students

class StudentForms(forms.ModelForm):
    class Meta:
        model = students
        fields = ('studentName','StudentFaculty')