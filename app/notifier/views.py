from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from notifier.models import Notification
from notifier.serializers import NotificationSerializer


class NotificationViewSet(viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def get_queryset(self):
        """ Returns objects for the authenticated user only """
        return Notification.objects.all().filter(user=self.request.user)



