from notifier import models
from datetime import datetime
from django.test import TestCase


class TestNotifierModels(TestCase):
    def test_team_model_representation(self):
        team_name = "River Plate"
        model = models.Team.objects.create(
            team_id="2",
            name=team_name
        )

        assert str(model) == team_name

    def test_tournament_model_representation(self):
        tour_name = "Liga Profesional de Fútbol"
        model = models.Tournament.objects.create(
            tour_id="2",
            name=tour_name
        )

        assert str(model) == tour_name

    def test_notif_representation(self):
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

    def test_fixture_representation(self):
        team_name = "River Plate"
        league_name = "Liga Profesional de Fútbol"
        team = models.Team.objects.create(
            team_id="2",
            name=team_name
        )
        tour = models.Tournament.objects.create(
            tour_id="2",
            name=league_name
        )

        season = "2021"
        date = datetime.strptime("10/03/2022 12:00:00", "%d/%m/%Y %H:%M:%S")

        fixture = models.Fixture.objects.create(
            team=team,
            league=tour,
            season=season,
            date=date
        )

        print(fixture)
