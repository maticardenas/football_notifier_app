from django.urls import path, include
from rest_framework.routers import DefaultRouter

from notifier import views

router = DefaultRouter()
router.register("notifications", views.NotificationViewSet)

app_name = "notifier"

urlpatterns = [
    path("", include(router.urls))
]