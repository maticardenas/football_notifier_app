from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import User
from notifier.models import NotifSubscription, Team


def test_login_required(api_client: APIClient):
    # given - when
    notifier_list_url = reverse("notifier:notifsubscription-list")
    response = api_client.get(notifier_list_url)

    # then
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_retrieve_notif_subscriptions(
        user: User, api_client: APIClient, notif_subscription: NotifSubscription
):
    # given
    notifier_list_url = reverse("notifier:notifsubscription-list")
    api_client.force_authenticate(user)

    # when
    response = api_client.get(notifier_list_url)

    # then
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'id': 1, 'user': user.id, 'team': 4, 'season': 2022}]


def test_create_notif_subscription(
        user: User, api_client: APIClient, team: Team
):
    # given
    notifier_list_url = reverse("notifier:notifsubscription-list")
    api_client.force_authenticate(user)
    notif_subscription = {'user': user.id, 'team': team.id, 'season': 2022}

    # when
    response = api_client.post(notifier_list_url, data=notif_subscription)

    # then
    assert response.status_code == status.HTTP_201_CREATED
    created_notif_subscription = response.json()
    created_notif_subscription.pop("id")
    assert response.json() == {'user': user.id, 'team': team.id, 'season': 2022}
