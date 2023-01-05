from django.urls import path
from student import views

urlpatterns = [
    path('student_list/', views.StudentList.as_view()),
    path('student_create/', views.StudentCreate.as_view()),
    path('student_retrieve/<int:pk>/', views.StudentRetrieve.as_view()),
    path('student_update/<int:pk>/', views.StudentUpdate.as_view()),
    path('student_destroy/<int:pk>/', views.StudentDestroy.as_view()),
]
