from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase

from core.models import User
from notifier.models import Notification

NOTIFIER_URL = reverse("notifier:notification-list")



def test_login_required(api_client: APIClient):
    response = api_client.get(NOTIFIER_URL)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_retrieve_notifications(
        user: User, api_client: APIClient, notification: Notification):
    api_client.force_authenticate(user)
    response = api_client.get(NOTIFIER_URL)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {'id': 1, 'team': 1, 'league': 1, 'season': '2022'}]

def test_retrieve_notifications(
        user: User, api_client: APIClient, notification: Notification):
    api_client.force_authenticate(user)

    payload = {}


    response = api_client.post(NOTIFIER_URL)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {'id': 1, 'team': 1, 'league': 1, 'season': '2022'}]

