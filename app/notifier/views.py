from notifier.models import NotifSubscription
from notifier.serializers import NotifSubscriptionSerializer
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class TeamViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class NotifSubscriptionViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = NotifSubscriptionSerializer

    queryset = NotifSubscription.objects.all()

    def get_queryset(self):
        return NotifSubscription.objects.filter(user__name=self.request.user.name)

    def perform_create(self, serializer: NotifSubscriptionSerializer):
        serializer.save(user=self.request.user)