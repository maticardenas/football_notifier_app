from django.urls import include, path
from notifier import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("notification", views.NotificationViewSet)
router.register("notification/subscribe", views.NotifSubscriptionViewSet)

app_name = "notifier"

urlpatterns = [
    path("", include(router.urls)),
]
