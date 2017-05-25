from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import UserProfile, Game, Achievement, Clan

class UserProfileSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='userprofile-detail')
    user = CharField(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('url','user', 'steam_id','nickname', 'real_name', 'city','stateOrProvince',
        'country','url_profile', 'friends')
class GameSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='game-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Game
        fields = ('url','user', 'appid','name', 'version', 'company','opinion')
class AchievementSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='achievement-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Achievement
        fields = ('url','user', 'appid_game','name', 'achieved')

class ClanSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='clan-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Clan
        fields = ('url','user', 'name','number_of_person', 'members')