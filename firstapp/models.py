from django.db import models

# Create your models here.


class students(models.Model):
    studentName=models.CharField(max_length=255)
    StudentFaculty=models.CharField(max_length=255)
    CreatedAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)
