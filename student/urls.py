from django.urls import path
from . import views

urlpatterns = [
    path('', views.SchoolClass.as_view()),
]
