from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import json

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    steam_id = models.IntegerField(blank=True, null = True)
    name = models.CharField(max_length=50, blank=True, null=True)
    real_name=models.CharField(max_length=50, blank=True, null=True)
    country=models.CharField(max_length=50, blank=True, null=True)
    url_profile=models.CharField(max_length=50, blank=True, null=True)
    avatar=models.CharField(max_length=50, blank=True, null=True)
    friends=models.ManyToManyField('self', null=True, blank=True)

    def __unicode__(self):
        return str(self.user.username)

class Game (models.Model):
    user = models.ForeignKey(User)
    appid = models.IntegerField(blank=True,  null = True)
    name = models.CharField(max_length=50, blank=True, null=True)
    version= models.FloatField(blank=True, null=True)
    company=models.CharField(max_length=50, blank=True, null=True)
    news = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return str("Usuario: " + self.user.username + "," + "Juego: " + str(self.name))


class Achievement(models.Model):
    user = models.ForeignKey(User)
    appid_game = models.ForeignKey(Game, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    achieved = models.BooleanField(default=False)
    def __unicode__(self):
        return str("Usuario: " + self.user.username + "," + "Achievement: "+ self.name)


class Clan(models.Model):
    user = models.ForeignKey(User)
    id_clan=models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    number_of_person=models.IntegerField(blank=True, null=True)
    members = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return str(self.name)