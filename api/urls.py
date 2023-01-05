from student.views import StudentReadOnlyModelViewSet
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi', StudentReadOnlyModelViewSet, basename='student')

urlpatterns = router.urls
