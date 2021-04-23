from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    DocumentViewSet,
    DriverProfileViewSet,
    InviteCodeViewSet,
    NotificationViewSet,
    UserProfileViewSet,
)

router = DefaultRouter()
router.register("notification", NotificationViewSet)
router.register("userprofile", UserProfileViewSet)
router.register("document", DocumentViewSet)
router.register("driverprofile", DriverProfileViewSet)
router.register("invitecode", InviteCodeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
