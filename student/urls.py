from django.urls import path
from student import views

urlpatterns = [
    path('lc/', views.StudentListCreate.as_view()),
    path('ru/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    path('rd/<int:pk>/', views.StudentRetrieveDestroy.as_view()),
    path('rud/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
]
