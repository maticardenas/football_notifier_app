# Generated by Django 2.1.15 on 2022-05-14 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0021_auto_20220513_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamstanding',
            name='goals_diff',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teamstanding',
            name='points',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teamstanding',
            name='rank',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
