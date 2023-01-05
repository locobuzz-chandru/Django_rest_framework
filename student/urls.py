from django.urls import path
from student import views

urlpatterns = [
    path('list/', views.StudentList.as_view()),
    path('create/', views.StudentCreate.as_view()),
    path('retrieve/<int:pk>/', views.StudentRetrieve.as_view()),
    path('update/<int:pk>/', views.StudentUpdate.as_view()),
    path('destroy/<int:pk>/', views.StudentDestroy.as_view()),
]
