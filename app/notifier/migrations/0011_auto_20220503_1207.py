# Generated by Django 2.1.15 on 2022-05-03 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifier", "0010_auto_20220503_1123"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notification",
            name="league",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="team",
        ),
        migrations.RemoveField(
            model_name="notifsubscription",
            name="notif",
        ),
        migrations.AddField(
            model_name="notifsubscription",
            name="season",
            field=models.IntegerField(default=2022),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="notifsubscription",
            name="team",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="notifier.Team",
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="Notification",
        ),
    ]
