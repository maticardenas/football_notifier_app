import pytest
from core.models import User
from django.contrib.auth import get_user_model
from notifier.models import NotifSubscription, Team, Tournament
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user() -> User:
    user = get_user_model().objects.create_user("test@notifier.com", "password123")
    yield user
    user.delete()


@pytest.fixture
def team() -> Team:
    return Team.objects.create(team_id="1", name="River Plate")


@pytest.fixture
def league():
    return Tournament.objects.create(tour_id="1", name="Liga Profesional de Futbol")


@pytest.fixture
def notif_subscription(team: Team, user: User):
    notif_subscrition = NotifSubscription.objects.create(team=team, user=user, season="2022")
    yield notif_subscrition
    notif_subscrition.delete()
