from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game (models.Model):
    game_id = models.IntegerField()
    name = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 20)
    #achievements = [models.CharField(max_length= 30)]

class UserProfile (models.Model):
    user = models.OneToOneField(User)
    apikey = models.CharField(max_length = 100)
    user_id = models.IntegerField()
    name = models.CharField(max_length = 30)
    games = models.ManyToManyField(Game)
    #games = [models.ForeignKey(Game)]
    friends = models.ManyToManyField(User)
    #friends = [models.ForeignKey(User)]
    achievements =[models.charField(max_length = 30)]

    def __unicode__(self):
        return self.name

class Admin:
    pass


class Sobre(models.Model):
    date = models.DateTimeField()
    amount = models.IntegerField()
    concept = models.TextField(max_length=100)
    donor = models.ForeignKey(Donor)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.donor.name+" - "+self.concept
