from django.db import models

from app import settings


class Team(models.Model):
    team_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True)
    picture = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class League(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TeamStanding(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE,)
    league = models.ForeignKey(League, on_delete=models.CASCADE,)
    season = models.CharField(max_length=255)
    rank = models.CharField(max_length=255, null=True)
    points = models.CharField(max_length=255, null=True)
    goals_diff = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.league.name} - {self.team.name} - {self.rank}"


class Fixture(models.Model):
    home_team = models.ForeignKey(
        Team,
        related_name="%(class)s_home_team",
        on_delete=models.CASCADE,
    )
    away_team = models.ForeignKey(
        Team,
        related_name="%(class)s_away_team",
        on_delete=models.CASCADE,
    )
    league = models.ForeignKey(
        League,
        on_delete=models.CASCADE,
    )
    season = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    goals_home = models.CharField(max_length=255, null=True)
    goals_away = models.CharField(max_length=255, null=True)
    round = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.home_team} vs. {self.away_team} - {self.league} - {self.round} - {self.date} - {self.season}"


class Score(models.Model):
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()


class NotifSubscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )
    season = models.IntegerField()

    def __str__(self):
        return f"{self.user.name} - {self.team.name} - {self.season}"
