from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(unique=True)
    city = models.CharField(max_length=50)


class School(models.Model):
    student = models.ManyToManyField(Student)
    school_name = models.TextField()
    joined_on = models.DateTimeField(auto_now_add=True)
