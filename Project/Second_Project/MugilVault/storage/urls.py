from rest_framework.routers import DefaultRouter
from storage.views import FileViewSet

router = DefaultRouter()
router.register('files', FileViewSet, basename="files")

urlpatterns = router.urls
