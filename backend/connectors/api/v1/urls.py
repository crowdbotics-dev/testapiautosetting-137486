from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137486ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137486", Testconnectors137486ViewSet, basename="testconnectors137486"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
