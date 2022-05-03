from notifier.models import Notification, NotifSubscription
from notifier.serializers import NotificationSerializer, \
    NotifSubscriptionSerializer
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class TeamViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class NotificationViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def perform_create(self, serializer: NotificationSerializer):
        serializer.save(user=self.request.user)


class NotifSubscriptionViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = NotifSubscriptionSerializer
    queryset = NotifSubscription.objects.all()

    def perform_create(self, serializer: NotifSubscriptionSerializer):
        serializer.save(user=self.request.user)