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



