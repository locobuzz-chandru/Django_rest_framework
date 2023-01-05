from django.urls import path
from student import views

urlpatterns = [
    path('lc/', views.LCapi.as_view()),
    path('rud/<int:pk>/', views.RUDapi.as_view()),
]
