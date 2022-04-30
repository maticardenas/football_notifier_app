# Generated by Django 2.1.15 on 2022-02-25 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifier", "0002_notification_notifsubscription"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fixture",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("season", models.CharField(max_length=255)),
                ("date", models.DateTimeField()),
                (
                    "league",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="notifier.Tournament",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="notifier.Team"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Score",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("home_goals", models.IntegerField()),
                ("away_foals", models.IntegerField()),
                (
                    "fixture",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="notifier.Fixture",
                    ),
                ),
            ],
        ),
    ]
