import pytest
from core.models import User
from django.contrib.auth import get_user_model
from notifier.models import Notification, Team, Tournament
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user() -> User:
    return get_user_model().objects.create_user("test@notifier.com", "password123")


@pytest.fixture
def team() -> Team:
    return Team.objects.create(team_id="1", name="River Plate")


@pytest.fixture
def league():
    return Tournament.objects.create(tour_id="1", name="Liga Profesional de Futbol")


@pytest.fixture
def notification(team: Team, league: Tournament):
    return Notification.objects.create(team=team, league=league, season="2022")
