from datetime import datetime

from django.contrib.auth import get_user_model
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

    def test_notif_subscription_representation(self):
        # given
        team_name = "River Plate"
        team = models.Team.objects.create(team_id="2", name=team_name)
        user = get_user_model().objects.create_user(
            email="test@matias.com", password="testpass", name="Matias Test"
        )

        # when
        notif_subscription = models.NotifSubscription.objects.create(
            user=user, team=team, season="2022"
        )

        # then
        assert str(notif_subscription) == "Matias Test - River Plate - 2022"

    def test_fixture_representation(self):
        # given
        home_team_name = "River Plate"
        away_team_name = "Boca Juniors"
        home_team = models.Team.objects.create(team_id="2", name=home_team_name)
        away_team = models.Team.objects.create(team_id="3", name=away_team_name)
        league = "Liga Profesional de Fútbol"
        season = "2021"
        date = datetime.strptime("10/03/2022 12:00:00", "%d/%m/%Y %H:%M:%S")

        # when
        fixture = models.Fixture.objects.create(
            home_team=home_team,
            away_team=away_team,
            league=league,
            season=season,
            date=date,
        )

        # then
        assert (
            str(fixture)
            == "River Plate vs. Boca Juniors - Liga Profesional de Fútbol - 2022-03-10 12:00:00 - 2021"
        )
