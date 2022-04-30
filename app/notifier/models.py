from django.db import models

from app import settings


class Tournament(models.Model):
    tour_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Team(models.Model):
    team_id = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Fixture(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )
    league = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE,
    )
    season = models.CharField(max_length=255)
    date = models.DateTimeField()


class Score(models.Model):
    fixture = models.ForeignKey(
        Fixture,
        on_delete=models.CASCADE
    )
    home_goals = models.IntegerField()
    away_foals = models.IntegerField()


class Notification(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )
    league = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE,
    )
    season = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.team.name} - {self.league.name} - {self.season}"


class NotifSubscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    notif = models.ForeignKey(
        Notification,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.notif)
