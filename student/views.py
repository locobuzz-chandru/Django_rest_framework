from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Student, School
from .serializers import StudentSerializer, SchoolSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from .utils import RedisSchool
import logging
from django.shortcuts import render
from .tasks import send_mail_func


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


# class SchoolModelViewSet(viewsets.ModelViewSet):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
# authentication_classes = [JWTAuthentication]
# permission_classes = [IsAuthenticated]


class SchoolClass(APIView):
    def post(self, request):
        try:
            serializer = SchoolSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            RedisSchool().save(request.data.get('student'), serializer.data)
            return Response({"message": "School Added", "status": 201, "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception(e)
            return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            # school = School.objects.filter(student=request.data.get('student'))
            # serializer = SchoolSerializer(school, many=True)
            redis_data = RedisSchool().get(request.data.get('student'))
            send_mail_func.delay()
            return HttpResponse('sent')
            # return Response({"message": "Data Retrieved", "status": 200, "data": redis_data.values()},
            #                 status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            school_object = School.objects.get(id=request.data.get('id'))
            serializer = SchoolSerializer(school_object, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            RedisSchool().update(serializer.data, request.data.get('student'))
            return Response({"message": "School Updated", "status": 201, "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception(e)
            return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            school_object = School.objects.get(id=request.data.get('id'))
            school_object.delete()
            RedisSchool().delete(request.data.get('student'), request.data.get('id'))
            return Response({"message": "School Deleted", "status": 204, "data": {}},
                            status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logging.exception(e)
            return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)


# celery -A api.celery worker --pool=solo -l info
# celery -A api beat -l INFO
# celery -A api beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
