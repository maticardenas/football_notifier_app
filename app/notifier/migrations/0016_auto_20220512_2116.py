# Generated by Django 2.1.15 on 2022-05-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifier", "0015_auto_20220512_2101"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fixture",
            name="date",
            field=models.CharField(max_length=255),
        ),
    ]
