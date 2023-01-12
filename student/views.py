from .models import Student, School
from .serializers import StudentSerializer, SchoolSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class SchoolModelViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
