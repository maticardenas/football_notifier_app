from django.test import TestCase
from notifier import models



def test_team_model_representation():
    team_name = "River Plate"
    model = models.Team.create(
        id="2",
        name=team_name
    )

    assert str(model) == team_name


def test_tournament_model_repreentation():
    tour_name = "Liga Profesional de Fútbol"
    model = models.Tournament.create(
        id="2",
        name=tour_name
    )

    assert str(model) == tour_name
