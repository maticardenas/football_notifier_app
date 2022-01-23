import pytest
from django.test import TestCase
from notifier import models


@pytest.fixture(autouse=True)
def db(request, django_db_setup, django_db_blocker):
    django_db_blocker.unblock()


def test_team_model_representation():
    team_name = "River Plate"
    model = models.Team.objects.create(
        team_id="2",
        name=team_name
    )

    assert str(model) == team_name


def test_tournament_model_representation():
    tour_name = "Liga Profesional de Fútbol"
    model = models.Tournament.objects.create(
        tour_id="2",
        name=tour_name
    )

    assert str(model) == tour_name

def test_notif_representation():
    team_name = "River Plate"
    tour_name = "Liga Profesional de Fútbol"
    team = models.Team.objects.create(
        team_id="2",
        name=team_name
    )
    tour = models.Tournament.objects.create(
        tour_id="2",
        name=tour_name
    )

    notif = models.Notification.objects.create(
        team=team,
        league=tour,
        season="2021"
    )

    assert str(notif) == f"{team_name} - {tour_name} - 2021"
