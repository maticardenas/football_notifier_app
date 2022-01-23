from django.db import models


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