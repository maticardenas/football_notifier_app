# Generated by Django 2.1.15 on 2022-05-02 19:43

from django.db import migrations

TEAMS = [
    {"team_id": 435, "name": "River Plate", "description": "Best Team Ever"},
    {"team_id": 85, "name": "PSG", "description": "Paris Saint Germain"},
    {"team_id": 26, "name": "Seleccion Argentina", "description": "AFA"},
]


def create_teams(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Team = apps.get_model("notifier", "Team")

    for team in TEAMS:
        team_to_create = Team()
        team_to_create.team_id = team["team_id"]
        team_to_create.name = team["name"]
        team_to_create.description = team["description"]
        team_to_create.save()


class Migration(migrations.Migration):

    dependencies = [
        ("notifier", "0008_tournament_country"),
    ]

    operations = [
        migrations.RunPython(
            create_teams,
        )
    ]
