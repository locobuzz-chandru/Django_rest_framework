from django.urls import path
from student import views

urlpatterns = [
    path('lc1/', views.ListCreateStudentAPI.as_view()),
    path('rud1/<int:pk>/', views.ReadUpdateDeleteStudentAPI.as_view()),
    path('lc2/', views.ListCreateSchoolAPI.as_view()),
    path('rud2/<int:pk>/', views.ReadUpdateDeleteSchoolAPI.as_view()),
]
