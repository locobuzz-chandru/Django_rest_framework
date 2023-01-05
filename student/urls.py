from django.urls import path
from student import views

urlpatterns = [
    path('lc/', views.StudentListCreate.as_view()),
    path('rud/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
]
