from rest_framework import routers

from .views import HotFileViewSet

router = routers.SimpleRouter()
router.register(r'hot-file', HotFileViewSet)
urlpatterns = router.urls