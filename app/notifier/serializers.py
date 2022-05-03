from notifier.models import Notification, NotifSubscription
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("id", "team", "league", "season")
        read_only_fields = ("id",)


class NotifSubscriptionSerializer(serializers.ModelSerializer):
    notification = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Notification.objects.all()
    )

    class Meta:
        model = NotifSubscription
        fields = ("id", "notification", "user")
        read_only_fields = ("id",)
