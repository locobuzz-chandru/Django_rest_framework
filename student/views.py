from rest_framework.permissions import AllowAny
from .models import Student, School
from .serializers import StudentSerializer, SchoolSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .custompermission import MyPermission


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]


class SchoolModelViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
