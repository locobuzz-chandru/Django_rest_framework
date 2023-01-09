from rest_framework import serializers
from .models import Student, School


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']


class SchoolSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = School
        fields = '__all__'
