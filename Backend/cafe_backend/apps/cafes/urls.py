from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CafeViewSet

router = DefaultRouter()
router.register(r"cafes", CafeViewSet, basename="cafe")

app_name = "cafes"
urlpatterns = [
    path("", include(router.urls)),
]
