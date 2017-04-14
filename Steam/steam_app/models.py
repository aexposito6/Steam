from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import json
# Create your models here.


class UserProfile (models.Model):
    user = models.OneToOneField(User)
    apikey = models.CharField(max_length = 100)
    id_user = models.IntegerField()

    def __unicode__(self):
        return self.user.username



