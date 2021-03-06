from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomTextViewSet,
    HomePageViewSet,
    NEW1ViewSet,
    R123ViewSet,
    R456ViewSet,
    R789ViewSet,
    TestViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("r789", R789ViewSet)
router.register("r123", R123ViewSet)
router.register("r456", R456ViewSet)
router.register("test", TestViewSet)
router.register("new1", NEW1ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
