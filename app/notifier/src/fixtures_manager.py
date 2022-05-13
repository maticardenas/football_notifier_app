from notifier.models import Fixture, Team, League
from notifier.src.api_clients.fixtures_client import FixturesClient


class FixturesManager:
    def __init__(self) -> None:
        self._fixtures_client = FixturesClient()

    def update_season_fixtures(self, team_id: int, season: int) -> None:
        team_season_fixture = self._fixtures_client.get_fixtures_by(season, team_id)

        fixtures = team_season_fixture.as_dict["response"]

        for fixture in fixtures:
            team_fixture = Fixture()
            home_team = fixture["teams"]["home"]
            team_fixture.home_team, created = Team.objects.get_or_create(
                team_id=home_team["id"],
                name=home_team["name"],
                picture=home_team["logo"]
            )
            away_team = fixture["teams"]["away"]
            team_fixture.away_team, created = Team.objects.get_or_create(
                team_id=away_team["id"],
                name=away_team["name"],
                picture=away_team["logo"]
            )
            team_fixture.league, created = League.objects.get_or_create(
                name=fixture["league"]["name"],
                country=fixture["league"]["country"],
                round=fixture["league"]["round"],
                logo=fixture["league"]["logo"]
            )
            team_fixture.date = fixture["fixture"]["date"]
            team_fixture.season = season
            team_fixture.goals_home = fixture["goals"]["home"]
            team_fixture.goals_away = fixture["goals"]["away"]
            team_fixture.save()


fixtures_manager = FixturesManager()
fixtures_manager.update_season_fixtures(435, 2022)