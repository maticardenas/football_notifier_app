from datetime import datetime

from django.test import TestCase
from notifier import models


class TestNotifierModels(TestCase):
    def test_team_representation(self):
        # given
        team_name = "River Plate"

        # when
        model = models.Team.objects.create(team_id="2", name=team_name)

        # then
        assert str(model) == team_name

    def test_tournament_representation(self):
        # given
        tour_name = "Liga Profesional de Fútbol"

        # when
        model = models.Tournament.objects.create(tour_id="2", name=tour_name)

        # then
        assert str(model) == tour_name

    def test_notif_representation(self):
        # given
        team_name = "River Plate"
        tour_name = "Liga Profesional de Fútbol"
        team = models.Team.objects.create(team_id="2", name=team_name)
        tour = models.Tournament.objects.create(tour_id="2", name=tour_name)

        # when
        notif = models.Notification.objects.create(
            team=team, league=tour, season="2021"
        )

        # then
        assert str(notif) == f"{team_name} - {tour_name} - 2021"

    def test_fixture_representation(self):
        # given
        home_team_name = "River Plate"
        away_team_name = "Boca Juniors"
        league_name = "Liga Profesional de Fútbol"
        home_team = models.Team.objects.create(team_id="2", name=home_team_name)
        away_team = models.Team.objects.create(team_id="3", name=away_team_name)
        tour = models.Tournament.objects.create(tour_id="2", name=league_name)
        season = "2021"
        date = datetime.strptime("10/03/2022 12:00:00", "%d/%m/%Y %H:%M:%S")

        # when
        fixture = models.Fixture.objects.create(
            home_team=home_team,
            away_team=away_team,
            league=tour,
            season=season,
            date=date,
        )

        # then
        assert (
            str(fixture)
            == "River Plate vs. Boca Juniors - Liga Profesional de Fútbol - 2022-03-10 12:00:00 - 2021"
        )
