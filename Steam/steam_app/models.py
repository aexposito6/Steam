from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    steam_id = models.IntegerField(blank=True, null = True, unique=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    real_name=models.CharField(max_length=50, blank=True, null=True)
    country=models.CharField(max_length=50, blank=True, null=True)
    url_profile=models.CharField(max_length=50, blank=True, null=True)
    avatar=models.CharField(max_length=50, blank=True, null=True)
    friends=models.TextField(null=True, blank=True) #Para poder poner amigos que no esten registrados a nuestra app

    def __unicode__(self):
        return str(self.user.username)

class Game (models.Model):
    user = models.ForeignKey(User)
    appid = models.IntegerField(blank=True,  null = True)
    name = models.CharField(max_length=50, blank=True, null=True)
    version= models.FloatField(blank=True, null=True)
    company=models.CharField(max_length=50, blank=True, null=True)
    opinion = models.TextField(null=True, blank=True)
    def get_absolute_url(self):
        return reverse('change_name', kwargs={'id_game': self.id})
    def __unicode__(self):
        return str( "Juego: " + str(self.name) + "," + str(self.id))


class Achievement(models.Model):
    #user = models.ForeignKey(UserProfile)
    user = models.ForeignKey(User)
    appid_game = models.ForeignKey(Game, default=False)
    name = models.CharField(max_length=50, default='')
    achieved = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse('change_achievement', kwargs={'id_achievement': self.id})
    def __unicode__(self):
        return str("Usuario: " + str(self.user) + "," + "Achievement: "+ str(self.name))


class Clan(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50, default='')
    number_of_person=models.IntegerField(blank=True, null=True)
    members = models.TextField(null=True, blank=True) #Para poder poner miembros que no esten regitrados a nuestra app
    def get_absolute_url(self):
        return reverse('change_clan', kwargs={'id_clan': self.id})
    def __unicode__(self):
        return str("Clan:" + self.name + "," + str(self.id))