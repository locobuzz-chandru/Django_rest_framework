from django.urls import path, include
from student.views import StudentModelViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('student', StudentModelViewSet, basename='student')
# router.register('school', SchoolModelViewSet, basename='school')


urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refreshtoken/', TokenRefreshView.as_view()),
    path('verifytoken/', TokenVerifyView.as_view()),
    path('schoolapi/', include('student.urls')),
]
