from rest_framework import routers
from .viewsets import DinosaurViewSet

router = routers.DefaultRouter()
router.register('api/dinosaur', DinosaurViewSet, 'dinosaur')

urlpatterns = router.urls
