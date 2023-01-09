from django.urls import path
from student import views

urlpatterns = [
    path('lc1/', views.LCStudentAPI.as_view()),
    path('rud1/<int:id>/', views.RUDStudentAPI.as_view()),
    path('lc2/', views.LCSchoolAPI.as_view()),
    path('rud2/<int:pk>/', views.RUDSchoolAPI.as_view()),
]
