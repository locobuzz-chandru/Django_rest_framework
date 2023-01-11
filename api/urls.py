from django.urls import path, include

from student.views import StudentModelViewSet, SchoolModelViewSet
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('student', StudentModelViewSet, basename='student')
router.register('school', SchoolModelViewSet, basename='school')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
