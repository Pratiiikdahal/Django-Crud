from django.contrib import admin
from firstapp.models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('studentName','StudentFaculty','CreatedAt','updatedAt')
    list_per_page=3
    
admin.site.register(students,StudentAdmin)