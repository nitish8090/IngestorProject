from rest_framework import routers

from .views import StacViewSet

router = routers.SimpleRouter()
router.register(r'stac', StacViewSet, basename='stac')
urlpatterns = router.urls