from notifier.src.fixtures_manager import FixturesManager


def update():
    fixtures_manager = FixturesManager()
    fixtures_manager.update_team_standings(435, 2022)