from student.views import StudentModelViewSet
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi', StudentModelViewSet, basename='student')

urlpatterns = router.urls
