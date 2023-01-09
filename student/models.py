from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)


class School(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    school_name = models.TextField()
    joined_at = models.DateTimeField(auto_now_add=True)
