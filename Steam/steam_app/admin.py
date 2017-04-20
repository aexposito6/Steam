from django.contrib import admin

# Register your models here.
from models import UserProfile

from django.contrib import admin

# Register your models here.
from models import UserProfile, Game, Achievement, Clan

admin.site.register(UserProfile)
admin.site.register(Game)
admin.site.register(Achievement)
admin.site.register(Clan)