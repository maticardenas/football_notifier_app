from django.db import migrations
from notifier.src.fixtures_manager import FixturesManager


def populate_fixture(apps, schema_editor):
    fixtures_manager = FixturesManager()
    fixtures_manager.update_season_fixtures(435, 2022)


class Migration(migrations.Migration):

    dependencies = [
        ("notifier", "0020_auto_20220514_1801"),
    ]

    operations = [
        migrations.RunPython(
            populate_fixture,
        )
    ]
