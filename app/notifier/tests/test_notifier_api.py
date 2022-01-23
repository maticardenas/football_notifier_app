import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from notifier.models import Notification, Team, Tournament

from core.models import User

NOTIFIER_URL = reverse("notifier:notifications")


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user() -> User:
    return get_user_model().objects.create_user(
        "test@notifier.com",
        "password123"
    )

@pytest.fixture
def team() -> Team:
    return Team.objects.create(
        "1",
        "River Plate"
    )

@pytest.fixture
def league():
    return Tournament.objects.create(
        "1",
        "Liga Profesional de Futbol"
    )


@pytest.fixture
def notification(team: Team, league: Tournament):
    return Notification.objects.create(
        team=team,
        league=league,
        season="2022"
    )

def test_login_required(api_client: APIClient):
    response = api_client.get(NOTIFIER_URL)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_retrieve_notifications(user: User, api_client: APIClient, notification: Notification):
    response = api_client.get(NOTIFIER_URL)

    notifications = Notification.objects.all()
    # serializer = NotificationSerializer()


