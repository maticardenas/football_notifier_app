from notifier.models import Notification
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("id", "team", "league", "season")
        read_only_fields = ("id",)
