from student.views import StudentViewSet
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi', StudentViewSet, basename='student')

urlpatterns = router.urls
