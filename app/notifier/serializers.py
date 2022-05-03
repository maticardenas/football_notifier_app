from notifier.models import NotifSubscription
from rest_framework import serializers


class NotifSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotifSubscription
        fields = ("id", "user", "team", "season")
        read_only_fields = ("id",)
